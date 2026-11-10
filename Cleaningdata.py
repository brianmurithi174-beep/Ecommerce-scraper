import pandas as pd

file_name = "correct_coastline_data.csv"

try:
    df = pd.read_csv(file_name)

    # --- THE FIX STARTS HERE ---
    print("Original Column Names:", df.columns.tolist())

    # We will forcefully rename the first two columns to keep things simple
    # This assumes Column 0 is the Country Name and Column 1 is the Coastline length
    df.rename(columns={
        df.columns[0]: 'Country',
        df.columns[1]: 'Coastline'
    }, inplace=True)

    print("New Column Names:", df.columns.tolist())
    # --- THE FIX ENDS HERE ---

    # Now your cleaning code will work because we GUARANTEED the name is 'Coastline'
    print("Cleaning data...")

    df['Coastline'] = (
        df['Coastline']
        .astype(str)
        .str.replace(',', '', regex=False)
        .str.replace(r'\[.*\]', '', regex=True)  # Removes [3], [note 1] etc
        .str.replace('-', '0', regex=False)
        .fillna(0)
    )

    # Convert to integers
    # We use to_numeric with 'coerce' to turn any remaining messy text into NaN (0), then fill with 0
    df['Coastline'] = pd.to_numeric(df['Coastline'], errors='coerce').fillna(0).astype(int)

    # Sort it
    sorted_df = df.sort_values(by='Coastline', ascending=False)

    print("\n--- Top 5 Countries by Coastline ---")
    print(sorted_df[['Country', 'Coastline']].head())

    # Save
    sorted_df.to_csv("cleaned_coastline_data.csv", index=False)
    print("\nSaved to cleaned_coastline_data.csv")

except Exception as e:
    print(f"Something went wrong: {e}")