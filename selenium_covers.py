import csv
import json
from webdriver_setup import get_driver
from amazon_scraper import AmazonBookScraper

def process_book_urls(urls):
    book_details_list = []
    with get_driver() as driver:
        scraper = AmazonBookScraper(driver)
        for url in urls:
            details = scraper.get_book_details(url)
            book_details_list.append(details)
    return book_details_list

def main():
    try:
        with open('books.csv', 'r') as csv_file:
            book_urls = [row[0].strip() for row in csv.reader(csv_file)]
        
        book_details_list = process_book_urls(book_urls)
        
        with open('book_details.json', 'w') as f:
            json.dump(book_details_list, f, indent=2)
        
        print(f"Book details saved to book_details.json")
    except Exception as e:
        print(f"Error during processing: {e}")

if __name__ == "__main__":
    main()
