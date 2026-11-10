import pdfplumber
import pandas as pd
import re


def clean_pab_data(pdf_path):
    all_agents = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Using 'text' strategy to find columns by alignment
            table = page.extract_table(table_settings={
                "vertical_strategy": "text",
                "horizontal_strategy": "text",
                "snap_tolerance": 4,
            })

            if not table: continue

            for row in table:
                # Filter out header rows or empty rows
                if not row or "Name" in str(row[0]): continue

                # We specifically look for P1D2 or P4 in any column
                # This fixes the "Shifting Column" error on Page 6 and 9
                license_type = None
                for cell in row:
                    if cell in ["P1D2", "P4"]:
                        license_type = cell
                        break

                if license_type:
                    all_agents.append({
                        "Full Name": row[0].replace('\n', ' ').strip() if row[0] else "",
                        "Agency": row[1].replace('\n', ' ').strip() if row[1] else "",
                        "Location": row[2].replace('\n', ' ').strip() if row[2] else "",
                        "License Type": license_type,
                        "Source": "Property Agents Board Register"
                    })

    df = pd.DataFrame(all_agents)
    # Final cleanup: Remove any accidental mainland addresses
    df = df[df['Location'].str.contains('Tasmania', case=False, na=False)]

    df.to_csv("tasmania_verified_agents.csv", index=False)
    print(f"Success! Saved {len(df)} verified agents to tasmania_verified_agents.csv")


# EXECUTE
clean_pab_data("C:/Users/hp/Downloads/individual_-_19_december_2025.pdf")