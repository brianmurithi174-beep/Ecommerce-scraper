from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your downloaded chromedriver
DRIVER_PATH = "C:/path/to/chromedriver.exe"  # <-- Change this to your path
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://web.whatsapp.com/")
print("Please scan the QR code with your phone and press Enter in this terminal.")
input()  # Pauses the script until you press Enter

# The contact or group name you want to message
contact_name = "Name of Contact or Group"
message = "Hello, this is a Selenium bot!"

try:
    # Wait for the search box to be available
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )

    # Search for the contact
    search_box.send_keys(contact_name)
    time.sleep(2)  # Wait for search results

    # Find the contact in the results and click it
    contact = driver.find_element(By.XPATH, f'//span[@title="{contact_name}"]')
    contact.click()

    # Wait for the message input box to load
    message_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
    )

    # Type the message and send
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

    print("Message sent successfully!")
    time.sleep(5)  # Wait a bit before closing

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()