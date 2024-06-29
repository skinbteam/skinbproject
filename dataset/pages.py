import requests
from bs4 import BeautifulSoup
import csv
import sys

def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def scrape_nivea_skincare_products():
    base_url = 'https://www.nivea.de'
    products_url = base_url + '/produkte'

    print(f"Fetching products page: {products_url}")
    soup = get_soup(products_url)

    if not soup:
        print("Failed to fetch the products page. Exiting.")
        return

    products = []
    page_number = 1
    max_pages = 500

    while True:
        # Find all product links on the current page
        product_links = soup.find_all('a', class_='nx-product-teaser__link-wrapper')

        excluded_keywords = ['haare', 'styling', 'deo', 'deodorant']

        for link in product_links:
            href = link['href']

            # Check if the link doesn't contain any excluded keywords
            if not any(keyword in href.lower() for keyword in excluded_keywords):
                full_url = base_url + href
                product_name = link.find('h6', class_='nx-product-teaser__headline').text.strip()
                products.append([product_name, full_url])

        # Check if there is a next page
        if page_number >= max_pages:
            print("Reached the maximum page limit.")
            break
        
        next_page_url = f"{products_url}?p={page_number + 1}"
        next_page_soup = get_soup(next_page_url)
        
        if next_page_soup and next_page_soup.find('a', class_='nx-product-teaser__link-wrapper'):
            print(f"Fetching next page: {next_page_url}")
            soup = next_page_soup
            page_number += 1
        else:
            break

    if products:
        # Save products to a CSV file
        with open('nivea_pages_products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name', 'URL'])
            writer.writerows(products)

        print(f"Scraped {len(products)} skincare products. Data saved to 'nivea_pages_products.csv'")
    else:
        print("No skincare products found. The website structure might have changed.")

    # Print the first few skincare products found (for debugging)
    print("\nFirst few skincare products found:")
    for product in products[:10]:
        print(f"{product[0]} - {product[1]}")

if __name__ == "__main__":
    scrape_nivea_skincare_products()