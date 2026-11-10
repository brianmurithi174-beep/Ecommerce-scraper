import pdfplumber
import pandas as pd


def extract_discovery_data(pdf_path):
    all_rows = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # We use a broader strategy to catch those 17 columns
            table = page.extract_table()
            if table:
                all_rows.extend(table)

    # We DON'T pass 'columns=' here to prevent the crash
    df = pd.DataFrame(all_rows)
    return df


# Run it and see what it finds
my_path = "C:/Users/hp/Downloads/individual_-_19_december_2025.pdf"  # Put your path here
df = extract_discovery_data(my_path)

# This will print the first 5 rows and the column count
print(f"I found {len(df.columns)} columns.")
print(df.head())

# Save it to a CSV so you can open it in Excel and see which columns are real
df.to_csv("pab_discovery.csv", index=False)