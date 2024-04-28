import os
import requests
from books_list import books 
from webdriver_setup import get_driver
from selenium.webdriver.common.by import By

def download_image(image_url, file_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return file_path
    else:
        return "Failed to download image"

def get_book_cover(url, title):
    sanitized_title = title.replace(' ', '_').replace("'", "").replace("-", "_")
    file_path = os.path.join('downloaded_covers', sanitized_title + '.jpg')
    
    if os.path.exists(file_path):
        return f"File already exists: {file_path}"

    try:
        with get_driver() as driver:
            driver.get(url)
            image_element = driver.find_element(By.ID, 'landingImage')
            if image_element:
                image_url = image_element.get_attribute('src')
                return download_image(image_url, file_path)
            else:
                return "No image found"
    except Exception as e:
        return f"Error: {e}"

try:
    for title, link in books:
        print(f"Cover Image URL for {title}: {get_book_cover(link, title)}")
except Exception as e:
    print(f"Error during processing: {e}")
