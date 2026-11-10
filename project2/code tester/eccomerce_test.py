import pandas as pd
import random
import time
from playwright.sync_api import sync_playwright, expect


class UniversalRetailScraper:
    def __init__(self, config):
        self.config = config
        self.results = []

    def human_delay(self):
        """Randomized pause to mimic human browsing."""
        time.sleep(random.uniform(3.0, 6.0))

    def run(self):
        with sync_playwright() as p:
            # 1. Launch with realistic headers
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            print(f"🚀 Navigating to {self.config['url']}...")
            # Use 'domcontentloaded' to bypass the 30s timeout issues
            page.goto(self.config['url'], wait_until="domcontentloaded", timeout=60000)

            page_num = 1
            while True:
                # --- STEP A: RE-LOCATE THE FINGERPRINT FRESH ---
                # We always re-find the element to avoid 'stale element' errors
                fingerprint_el = page.locator(self.config['fingerprint_selector']).first
                fingerprint_el.wait_for(state="visible", timeout=15000)

                old_value = fingerprint_el.inner_text().strip()
                old_url = page.url  # Track URL for pagination verification

                print(f"📥 Page {page_num} | Snapshot: {old_value[:35]}...")

                # --- STEP B: DATA EXTRACTION ---
                # Scroll to bottom first to ensure all lazy-loaded items appear
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                page.wait_for_timeout(2000)

                items = page.locator(self.config['item_container']).all()
                for item in items:
                    data = {}
                    for field, selector in self.config['fields'].items():
                        try:
                            el = item.locator(selector).first
                            if "link" in field.lower() or "url" in field.lower():
                                data[field] = el.get_attribute("href")
                            else:
                                data[field] = el.inner_text().strip()
                        except:
                            data[field] = None
                    self.results.append(data)

                # --- STEP C: THE PAGINATION TRIGGER ---
                next_btn = page.locator(self.config['next_button']).first
                if not next_btn.is_visible():
                    print("🏁 Next button missing. Reached end of list.")
                    break

                # Human-like interaction
                next_btn.scroll_into_view_if_needed()
                self.human_delay()
                next_btn.click()

                # --- STEP D: DUAL-VERIFICATION GUARD ---
                print("⏳ Waiting for data refresh...")
                try:
                    # Strategy 1: Check if URL changed (e.g., ?p=1 to ?p=2)
                    # We wait up to 5 seconds for a URL change
                    page.wait_for_url(lambda url: url != old_url, timeout=5000)
                    print("🌐 URL changed - confirmed new page.")
                except:
                    # Strategy 2: If URL didn't change (AJAX), wait for text change
                    try:
                        # We re-find the fingerprint FRESH to compare
                        expect(page.locator(self.config['fingerprint_selector']).first).not_to_have_text(old_value,
                                                                                                         timeout=10000)
                        print("✨ Content changed - confirmed new page.")
                    except:
                        print("⚠️ Guard failed: Content and URL are the same. Stopping.")
                        break

                page_num += 1

            browser.close()
            return pd.DataFrame(self.results).drop_duplicates()


# --- REUSABLE CONFIGURATION ---
if __name__ == "__main__":
    # Example for a retail site (iHerb context)
    retail_config = {
        'url': 'https://ke.iherb.com/c/supplements',
        'item_container': '.product-inner',  # The repeating product box
        'fingerprint_selector': '.product-title',  # The first product name
        'next_button': 'a.pagination-next',  # The specific Next link
        'fields': {
            'Name': '.product-title',
            'Price': '.price',
            'Link': 'a.product-link'
        }
    }

    scraper = UniversalRetailScraper(retail_config)
    df = scraper.run()

    if not df.empty:
        df.to_csv("retail_results.csv", index=False, encoding="utf-8-sig")
        print(f"✅ Success! Captured {len(df)} items.")