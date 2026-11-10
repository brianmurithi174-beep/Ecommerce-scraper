import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# URL you want to scrape
url = "https://en.wikipedia.org/wiki/List_of_countries_by_length_of_coastline"

# Set up the Chrome driver automatically
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

print("Loading page with Selenium...")
# Have the browser load the URL
driver.get(url)

# Wait a moment for the page to be fully loaded (optional but good practice)
time.sleep(2)

# Get the HTML source code of the page *after* it's loaded
html_source = driver.page_source

# Close the browser
driver.quit()
print("Browser closed.")
try:
    # 1. Read all tables
    tables = pd.read_html(html_source)
    print(f"Total tables found: {len(tables)}")

    target_table = None

    # 2. Loop through them to find the RIGHT one
    for i, df in enumerate(tables):
        # We convert column names to a string to check for keywords
        # We are looking for a table that actually has "Coastline" in the header
        if "Coastline" in str(df.columns) and len(df) > 10:
            print(f"Found the main table at Index [{i}]!")
            target_table = df
            break

    # 3. If we found it, save it
    if target_table is not None:
        # Wikipedia often has complex headers (MultiIndex).
        # This line flattens them into simple headers:
        target_table.columns = [' '.join(col).strip() for col in target_table.columns.values]

        # Now save
        target_table.to_csv("correct_coastline_data.csv", index=False)
        print("Success! Saved to 'correct_coastline_data.csv'")
        print(target_table.head())
    else:
        print("Could not find a table with 'Coastline' in the headers.")

except Exception as e:
    print(f"An error occurred: {e}")
