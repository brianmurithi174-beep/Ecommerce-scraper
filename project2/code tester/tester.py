import asyncio
from playwright.async_api import async_playwright
import pandas as pd


async def scrape_alhisba():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Target: Registered deals page
        await page.goto("https://alhisba.com/deals", wait_until="networkidle")

        # Select "Residential" (Arabic: سكني) from filter
        await page.click("text=سكني")
        await asyncio.sleep(2)  # Wait for JS refresh

        deals = []
        # Extracting the transaction table
        rows = await page.locator("tr.deal-row").all()  # Example selector

        for row in rows:
            data = await row.locator("td").all_text_contents()
            if len(data) > 5:
                deals.append({
                    "Area": data[0],  # Arabic Area Name
                    "Block": data[1],
                    "Size": data[2],  # e.g., "500 m2"
                    "Price": data[3],  # e.g., "450,000 KD"
                    "Date": data[4]
                })

        df = pd.DataFrame(deals)

        # Specialist Cleaning Logic
        df['Size_m2'] = df['Size'].str.replace('m2', '', case=False).str.strip().astype(float)
        df['Price_KD'] = df['Price'].str.replace('KD', '').str.replace(',', '').str.strip().astype(float)
        df['Price_per_sqm'] = df['Price_KD'] / df['Size_m2']

        # Export with UTF-8-SIG to preserve Arabic characters in Excel
        df.to_excel("Kuwait_Real_Estate_Deals.xlsx", index=False)
        print("Scraping and Cleaning Complete.")
        await browser.close()


asyncio.run(scrape_alhisba())