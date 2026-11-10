from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = Options()

# --- STEALTH FLAGS ---
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--start-maximized")
options.add_argument("--lang=en-US,en")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# --- REMOVE webdriver FLAG ---
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
)

driver.get("https://ke.iherb.com/c/baby-kids?p=1")
sleep(8)

print(driver.title)
