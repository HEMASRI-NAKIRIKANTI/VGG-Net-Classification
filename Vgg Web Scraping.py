import os
import time
import requests
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constant: Time to wait for the webpage to load
WEBPAGE_WAIT_TIME = 10
# Constant: Time to wait for job-related content to load on the webpage
JOB_LOAD_WAIT_TIME = 10
# Create a Chrome WebDriver instance
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
driver.set_window_size(1920, 1080)

# Define the URL of the Google Images search results page
url = 'https://www.google.com/search?q=book&tbm=isch'

# Send a request to the URL and get the response
driver.get(url)

# Scroll down to load more images (optional)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(50)  # Wait for the images to load

# Find all image elements on the page
image_elements = driver.find_elements(By.XPATH, '//div[@class="fR600b islir"]')

# Create a folder to store the images (if it doesn't exist)
folder_path = 'book_images'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Loop through each image element and download the image
for i, image_element in enumerate(image_elements):
    img_element = image_element.find_element(By.TAG_NAME, 'img')
    # Get the URL of the image
    image_url = image_element.get_attribute('src')
    # Get the source (URL) of the image
    img_src = img_element.get_attribute('src')
    print(img_src)
    # Check if the src attribute contains a base64 data URI
    if img_src and img_src.startswith('data:image/'):
        # Decode the base64-encoded data URI
        img_data = base64.b64decode(img_src.split(',')[1])
        img_filename = f'image_{i}.jpg'
        with open(os.path.join(folder_path, img_filename), 'wb') as f:
            f.write(img_data)

    elif img_src is not None:
        # Send a GET request to the image URL and save the response content to a file
        response = requests.get(img_src)
        img_filename = f'image_{i}.jpg'
        with open(os.path.join(folder_path, img_filename), 'wb') as f:
            f.write(response.content)

# Close the browser
driver.quit()
