import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from image_utils import download_image, sanitize_filename

class AmazonBookScraper:
    def __init__(self, driver):
        self.driver = driver

    def get_book_details(self, url):
        try:
            self.driver.get(url)
            
            title = self._get_title()
            sanitized_title = sanitize_filename(title)
            file_path = self._get_file_path(sanitized_title)
            
            self._download_cover_image(file_path)
            
            return {
                "title": title,
                "link": url,
                "path": file_path
            }
        except Exception as e:
            return {"error": f"Error: {e}"}

    def _get_title(self):
        title_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#productTitle"))
        )
        return title_element.text.strip()

    def _get_file_path(self, sanitized_title):
        return os.path.join('downloaded_covers', sanitized_title + '.jpg')

    def _download_cover_image(self, file_path):
        if os.path.exists(file_path):
            print(f"File {file_path} already exists")
            return
        
        image_element = self.driver.find_element(By.ID, 'landingImage')
        if image_element:
            image_url = image_element.get_attribute('src')
            download_image(image_url, file_path)
            print(f"Image downloaded successfully: {file_path}")
        else:
            print(f"Image not found for {file_path}")
