import pdfplumber
import pandas as pd
import re


def extract_verified_tas_agents(pdf_path):
    records = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            lines = [line.strip() for line in text.split("\n") if line.strip()]

            for line in lines:
                # -------- LICENSE ANCHOR --------
                license_match = re.search(r"\b(P1D2|P4)\b", line)
                if not license_match:
                    continue

                license_type = license_match.group(1)

                # -------- TASMANIA FILTER --------
                if not re.search(r"\bTAS\b|Tasmania", line, re.IGNORECASE):
                    continue

                # -------- NAME EXTRACTION --------
                # Name is always at the start until 2+ spaces
                name_match = re.match(r"^[A-Z][A-Za-z\s'.-]+", line)
                agent_name = name_match.group(0).strip() if name_match else ""

                # -------- AGENCY EXTRACTION --------
                agency_match = re.search(
                    r"\b(LJ Hooker|Ray White|Harcourts|Elders|First National|PRD|Raine & Horne|Independent)\b.*",
                    line,
                    re.IGNORECASE
                )
                agency_name = agency_match.group(0).strip() if agency_match else ""

                records.append({
                    "Agent Name": agent_name,
                    "Agency Name": agency_name,
                    "Location": "Tasmania",
                    "License Type": license_type,
                    "Source": "PAB Tasmania Register Dec 2025"
                })

    if not records:
        raise RuntimeError("No agents extracted. PDF text structure unexpected.")

    df = pd.DataFrame(records)
    df.to_csv("tasmania_verified_agents.csv", index=False)

    print(f"Verified {len(df)} agents.")
    print("File saved: tasmania_verified_agents.csv")


# RUN
extract_verified_tas_agents(
    r"C:/Users/hp/Downloads/individual_-_19_december_2025.pdf"
)
