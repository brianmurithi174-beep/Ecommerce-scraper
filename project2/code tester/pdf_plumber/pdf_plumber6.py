import pandas as pd
import re
from datetime import datetime


def normalize(text):
    return re.sub(r"\s+", " ", str(text)).strip()


def clean_agents_raw_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df.columns = ["raw_text"]

    cleaned_rows = []

    for raw in df["raw_text"]:
        line = normalize(raw)

        # -------- VALIDITY --------
        valid_match = re.search(r"\b(Yes|No)\b$", line)
        if not valid_match:
            continue
        validity = valid_match.group(1)
        line = line[:valid_match.start()].strip()

        # -------- EXPIRY DATE --------
        date_match = re.search(r"\b\d{2} \w{3} \d{4}\b$", line)
        if not date_match:
            continue
        expiry = datetime.strptime(date_match.group(), "%d %b %Y")
        line = line[:date_match.start()].strip()

        # -------- LICENSE TYPE --------
        lic_match = re.search(r"\b(P1D2|P4)\b$", line)
        if not lic_match:
            continue
        license_type = lic_match.group()
        line = line[:lic_match.start()].strip()

        # -------- ADDRESS (ends with postcode) --------
        addr_match = re.search(r"(.*\b\d{4})$", line)
        if not addr_match:
            continue
        address = addr_match.group(1)
        remaining = line[:addr_match.start()].strip()

        # -------- NAME & AGENCY SPLIT --------
        # Name always ends at first agency-looking phrase
        name_match = re.match(r"^[^,]+,\s+[^A-Z]*[A-Za-z()' .\-]+", remaining)
        if not name_match:
            continue

        name = normalize(name_match.group())
        agency = normalize(remaining[len(name):])

        # -------- TASMANIA FILTER --------
        if "Tasmania" not in address:
            continue

        cleaned_rows.append({
            "Agent Name": name,
            "Agency Name": agency,
            "Address": address,
            "License Type": license_type,
            "License Expiry": expiry.strftime("%Y-%m-%d"),
            "Valid": validity,
            "Source": "Property Agents Board Register"
        })

    result = pd.DataFrame(cleaned_rows)

    # -------- DEDUPLICATION --------
    result["key"] = (
        result["Agent Name"].str.lower().str.replace(r"[^a-z]", "", regex=True)
        + result["License Type"]
    )

    result = (
        result.drop_duplicates("key")
        .drop(columns="key")
    )

    result.to_csv(output_csv, index=False)
    print(f"Cleaned {len(result)} Tasmania agents → {output_csv}")


# RUN
clean_agents_raw_csv(
    "pab_discovery.csv",
    "agents.csv"
)
