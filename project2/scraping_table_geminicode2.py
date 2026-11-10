import pandas as pd
from playwright.sync_api import sync_playwright, expect

# --- CONFIGURATION ---
URL = "https://recursos.cpn.cr/colegiados/"
OUTPUT_CSV = "colegiados_complete.csv"

# 1. The Container ID
CONTAINER_SELECTOR = "#participants-list-1"

# 2. The Table (Sibling to the form inside the container)
TABLE_SELECTOR = f"{CONTAINER_SELECTOR} table.wp-list-table"

# 3. The Pagination Button - FIXED
# We now target the specific attribute title="Siguiente" seen in your error log
NEXT_BUTTON_SELECTOR = f"{CONTAINER_SELECTOR} .pagination a[title='Siguiente']"


def scrape_cpn_final():
    all_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print(f"🚀 Navigating to {URL}...")
        page.goto(URL, wait_until="networkidle")

        # Initial wait for table
        try:
            page.wait_for_selector(TABLE_SELECTOR, timeout=30000)
        except:
            print("🛑 Table not found. Check browser for CAPTCHA.")
            input("Press Enter once table is visible...")

        page_num = 1

        while True:
            # Re-locate table elements
            table = page.locator(TABLE_SELECTOR)
            rows = table.locator("tbody tr")

            if rows.count() == 0:
                print("⚠️ Table empty. Retrying...")
                page.wait_for_timeout(1000)
                if rows.count() == 0: break

            # --- 1. FINGERPRINT (Anti-Duplicate Logic) ---
            first_cell = rows.first.locator("td").first
            current_fingerprint = first_cell.inner_text().strip()

            print(f"📄 Scraping Page {page_num} (Row 1: {current_fingerprint})")

            # --- 2. EXTRACT DATA ---
            if page_num == 1:
                headers = [th.inner_text().strip() for th in table.locator("thead th").all()]

            for i in range(rows.count()):
                row = rows.nth(i)
                cells = row.locator("td").all()
                row_data = [c.inner_text().strip() for c in cells]

                if len(row_data) == len(headers):
                    all_data.append(dict(zip(headers, row_data)))

            # --- 3. PAGINATION ---
            next_btn = page.locator(NEXT_BUTTON_SELECTOR)

            # Check if button exists
            if not next_btn.is_visible():
                print("🏁 Next button not found. Scraping complete.")
                break

            # Click
            next_btn.click()

            # --- 4. WAIT FOR CHANGE (The Fix for Repetitive Scraping) ---
            try:
                # Wait until the name in the first row CHANGES
                expect(first_cell).not_to_have_text(current_fingerprint, timeout=15000)
            except:
                print("⚠️ Page content did not update. We may be at the end.")
                break

            page_num += 1

        browser.close()

    # --- SAVE ---
    if all_data:
        df = pd.DataFrame(all_data)
        df.drop_duplicates(inplace=True)
        df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
        print(f"✅ Scrape Complete! Saved {len(df)} rows to {OUTPUT_CSV}")
    else:
        print("❌ No data found.")


if __name__ == "__main__":
    scrape_cpn_final()