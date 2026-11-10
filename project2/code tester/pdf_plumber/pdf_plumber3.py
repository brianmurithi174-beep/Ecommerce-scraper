import pdfplumber
import pandas as pd


def extract_verified_tas_agents(pdf_path):
    all_agents = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # We use a loose extraction to get all text, then clean it manually
            table = page.extract_table()
            if not table: continue

            for row in table:
                # Clean the row: remove None and strip whitespace
                clean_row = [str(cell).replace('\n', ' ').strip() if cell else "" for cell in row]

                # ANCHOR LOGIC: Check if P1D2 or P4 exists anywhere in this row
                target_license = None
                if "P1D2" in clean_row:
                    target_license = "P1D2"
                elif "P4" in clean_row:
                    target_license = "P4"

                if target_license:
                    all_agents.append({
                        "Agent Name": clean_row[0],
                        "Agency Name": clean_row[1],
                        "Location": clean_row[2],
                        "License Type": target_license,
                        "Source": "PAB Tasmania Register Dec 2025"
                    })

    df = pd.DataFrame(all_agents)

    # Filter for Tasmania only (removes Victorian agents on the list)
    df = df[df['Location'].str.contains('Tasmania', case=False)]

    df.to_csv("tasmania_verified_agents.csv", index=False)
    print(f"Verified {len(df)} agents. File saved: 'tasmania_verified_agents.csv'")


# RUN THIS
extract_verified_tas_agents("C:/Users/hp/Downloads/individual_-_19_december_2025.pdf")