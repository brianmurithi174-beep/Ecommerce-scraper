from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://ke.iherb.com/c/baby-kids?p=1")
sleep(5)

print("Page title:", driver.title)


