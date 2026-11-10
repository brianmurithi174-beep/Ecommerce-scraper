import pdfplumber
import pandas as pd
import re
from datetime import datetime


TODAY = datetime.today()


def normalize(text: str) -> str:
    """Collapse excessive whitespace"""
    return re.sub(r"\s+", " ", text).strip()


def extract_verified_tas_agents(pdf_path):
    raw_lines = []

    # -------- STEP 1: READ & NORMALIZE ALL LINES --------
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            for line in text.split("\n"):
                line = normalize(line)
                if line:
                    raw_lines.append(line)

    # -------- STEP 2: MULTI-LINE RECORD RECONSTRUCTION --------
    records = []
    buffer = ""

    for line in raw_lines:
        # New record always starts with a name
        if re.match(r"^[A-Z][A-Za-z'().,\-\s]+,\s", line):
            if buffer:
                records.append(buffer)
            buffer = line
        else:
            buffer += " " + line

    if buffer:
        records.append(buffer)

    extracted = []

    # -------- STEP 3: FIELD EXTRACTION --------
    for record in records:
        confidence = 0

        # License anchor
        lic_match = re.search(r"\b(P1D2|P4)\b", record)
        if not lic_match:
            continue
        license_type = lic_match.group(1)
        confidence += 30

        # Tasmania filter
        if not re.search(r"Tasmania", record, re.IGNORECASE):
            continue
        confidence += 20

        # Expiry date
        date_match = re.search(r"\b(\d{2} \w{3} \d{4})\b", record)
        if not date_match:
            continue

        expiry = datetime.strptime(date_match.group(1), "%d %b %Y")
        if expiry < TODAY:
            continue
        confidence += 20

        # Agent name (from start until date)
        name_part = record.split(date_match.group(1))[0]
        agent_name = normalize(name_part)

        # Agency extraction (text between date and address)
        agency_part = record.split(date_match.group(1))[1]
        agency_match = re.search(
            r"([A-Za-z0-9@&().,'\- ]+?)\s+\d",
            agency_part
        )
        agency_name = normalize(agency_match.group(1)) if agency_match else ""

        if agency_name:
            confidence += 15

        # Address/location
        address_match = re.search(
            r"\d+.*Tasmania\s+\d{4}",
            record
        )
        location = normalize(address_match.group(0)) if address_match else "Tasmania"

        if location:
            confidence += 15

        extracted.append({
            "Agent Name": agent_name,
            "Agency Name": agency_name,
            "Location": location,
            "License Type": license_type,
            "License Expiry": expiry.strftime("%Y-%m-%d"),
            "Confidence Score": confidence,
            "Source": "PAB Tasmania Register Dec 2025"
        })

    # -------- STEP 4: DEDUPLICATION --------
    df = pd.DataFrame(extracted)

    df["dedupe_key"] = (
        df["Agent Name"].str.lower().str.replace(r"[^a-z]", "", regex=True) +
        df["License Type"]
    )

    df = (
        df.sort_values("Confidence Score", ascending=False)
          .drop_duplicates("dedupe_key")
          .drop(columns="dedupe_key")
    )

    df.to_csv("tasmania_verified_agents.csv", index=False)

    print(f"Verified {len(df)} agents.")
    print("File saved: Tasmania_agents2.csv")


# RUN
extract_verified_tas_agents(
    r"C:/Users/hp/Downloads/individual_-_19_december_2025.pdf"
)
