import os
import time
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
    sanitized_title = title.replace(' ', '_').replace("'", "").replace("-", "_").replace("!", "").replace("?", "")
    file_path = os.path.join('downloaded_covers', sanitized_title + '.jpg')
    book_details = (title, "")  # Initialize with title and empty description
    
    if os.path.exists(file_path):
        return f"File already exists: {file_path}"

    try:
        with get_driver() as driver:
            driver.get(url)
            image_element = driver.find_element(By.ID, 'landingImage')
            if image_element:
                image_url = image_element.get_attribute('src')
                download_image(image_url, file_path)
            driver.find_element(By.CSS_SELECTOR, "[data-a-expander-name='book_description_expander'] .a-expander-prompt").click()
            time.sleep(2)
            description_element = driver.find_element(By.CSS_SELECTOR, "[data-a-expander-name='book_description_expander']")
            if description_element:
                book_details = (title, description_element.text)
            else:
                return "No description found"
    except Exception as e:
        return f"Error: {e}"
    return book_details

try:
    book_details_list = []
    for title, link in books:
        details = get_book_cover(link, title)
        book_details_list.append(details)
    with open('book_descriptions.py', 'w') as f:
        f.write("book_descriptions = " + str(book_details_list))
except Exception as e:
    print(f"Error during processing: {e}")
