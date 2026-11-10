import pandas as pd
from playwright.sync_api import sync_playwright, expect

URL = "https://recursos.cpn.cr/colegiados/"
OUTPUT_FILE = "colegiados_data.csv"


def scrape_cpn():
    results = []

    with sync_playwright() as p:
        # headless=False allows you to solve CAPTCHA if it pops up
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print(f"🚀 Navigating to {URL}...")
        page.goto(URL, wait_until="networkidle")

        # Give the user a moment to handle any initial CAPTCHA
        page.wait_for_selector("table#table_1", timeout=60000)

        page_num = 1
        while True:
            print(f"📥 Scraping Page {page_num}...")

            # 1. Capture the 'Fingerprint' of the first row before clicking next
            # We use this to make sure the data actually updates
            first_cell_selector = "table#table_1 tbody tr:first-child td:first-child"
            current_first_cell_value = page.locator(first_cell_selector).inner_text().strip()

            # 2. Extract Table Headers (only once)
            if page_num == 1:
                headers = [th.inner_text().strip() for th in page.locator("table#table_1 thead th").all()]

            # 3. Extract Rows
            rows = page.locator("table#table_1 tbody tr").all()
            for row in rows:
                cells = [td.inner_text().strip() for td in row.locator("td").all()]
                if len(cells) == len(headers):
                    results.append(dict(zip(headers, cells)))

            # 4. Check for 'Next' button and click
            # DataTables uses 'next' class; if it's disabled, it usually has 'disabled' class
            next_button = page.locator("a#table_1_next")

            # If button is disabled or not visible, we are done
            if "disabled" in next_button.get_attribute("class") or not next_button.is_visible():
                print("🏁 Reached the last page.")
                break

            # 5. Click Next and WAIT for the content to change
            next_button.click()

            # This is the fix: Wait until the first cell NO LONGER contains the old value
            try:
                expect(page.locator(first_cell_selector)).not_to_have_text(current_first_cell_value, timeout=10000)
            except Exception:
                print("⚠️ Timeout waiting for page change. Content might be identical or site is slow.")
                break

            page_num += 1

        browser.close()

    # Export Data
    if results:
        df = pd.DataFrame(results)
        df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
        print(f"✅ Successfully saved {len(df)} records to {OUTPUT_FILE}")
    else:
        print("❌ No data found.")


if __name__ == "__main__":
    scrape_cpn()