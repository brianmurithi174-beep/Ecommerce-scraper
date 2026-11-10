import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# --- 1. Setup ---
# Create a folder to save images
output_folder = "scraped_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Set up the WebDriver (assumes chromedriver.exe is in your PATH)
driver = webdriver.Chrome()

# Get target URL from user
target_url = input("Enter the full website URL to scrape (e.g., https://www.example.com): ")
driver.get(target_url)

# --- 2. Handle Lazy Loading by Scrolling ---
print("Scrolling to the bottom to load all images...")
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for new images to load

    # Check if we've reached the bottom
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

print("Reached the bottom of the page.")

# --- 3. Find All Image URLs ---
print("Finding all image elements...")
image_elements = driver.find_elements(By.TAG_NAME, "img")
image_urls = []

for img in image_elements:
    src = img.get_attribute('src')

    # Check if 'src' exists and is a downloadable link
    if src and src.startswith(('http://', 'https://')):
        image_urls.append(src)

print(f"Found {len(image_urls)} downloadable images.")

# --- 4. Download Images ---
for i, url in enumerate(image_urls):
    try:
        # Get the image data
        response = requests.get(url, timeout=10)

        # Try to get a valid file extension
        # This is a simple way; complex URLs might not have extensions
        file_ext = os.path.splitext(url.split('/')[-1])[-1]
        if not file_ext or len(file_ext) > 5:  # Basic check for valid extension
            file_ext = ".jpg"  # Default to .jpg

        # Create a unique file name
        file_name = f"image_{i}{file_ext}"
        file_path = os.path.join(output_folder, file_name)

        # Save the image (in binary write mode)
        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"SUCCESS: Downloaded {url} -> {file_path}")

    except Exception as e:
        print(f"ERROR: Could not download {url}. Reason: {e}")

# --- 5. Cleanup ---
driver.quit()
print(f"\nDone! All images saved to the '{output_folder}' folder.")
