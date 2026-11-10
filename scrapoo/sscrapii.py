import containers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
website = "https://www.thesun.co.uk/sport/football/"
path = "C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Or, if you have a folder named 'chromedriver-win64' *inside* the downloads folder
# that contains *another* 'chromedriver-win64' folder:
# path = "C:/Users/hp/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# This one line automatically downloads and manages the correct chromedriver for you
driver = webdriver.Chrome()


driver.get(website)

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

container = driver.find_elements(by = "xpath", value = '//div[@class="story_copy-container"]')

# Find the <a> tags instead of the <h2> tags
links = driver.find_elements(by="xpath", value="//div[@class='story_copy-container']/a")
titles = []
link = []

# Loop through the <a> tags
for link_element in links:
    # 1. Get the title text from the <h2> inside the <a> tag
    # The XPath '.' means 'start from the current element' (the <a> tag)
    title_element = link_element.find_element(by="xpath", value=".//h2")
    title_text = title_element.text

    # 2. Get the link URL from the <a> tag itself
    url = link_element.get_attribute('href')

    print(f"Title: {title_text}")
    print(f"Link: {url}")
    print("---")