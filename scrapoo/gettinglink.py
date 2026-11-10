from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # For Chrome
# driver = webdriver.Firefox() # For Firefox

driver.get("https://www.thesun.co.uk/news/")