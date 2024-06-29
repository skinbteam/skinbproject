import csv

# Define a mapping of keywords to categories
category_keywords = {
    "face care": ["gesichtspflege", "make up", "gesichtsreinigung", "augencreme", "gesichtsserum"],
    "body care": ["körperpflege", "dusche & bad", "handcreme", "seife", "intimpflege"],
    "sun protection": ["sonnencreme fürs gesicht", "sonnenmilch", "sonnenspray", "kids", "after sun"],
    "men's care": ["gesicht", "rasur", "duschgel"],
    "nivea specials": ["parfum", "duftkerze", "luminous630® body ebenmäßiger hautton", "neu: nivea black & white invisible 72h"],
    "other": ["endlich sommer! denk an deinen sonnenschutz"]
}

def classify_product(product_name):
    """Classify the product based on keywords."""
    for category, keywords in category_keywords.items():
        if any(keyword.lower() in product_name.lower() for keyword in keywords):
            return category
    return "other"  # Default category if no keywords match

def classify_products(csv_file_path, output_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as infile, \
         open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write headers to the output file
        writer.writerow(['Product Name', 'URL', 'Category'])
        
        for row in reader:
            if not row:  # Skip empty rows
                continue
            product_name = row[0]
            product_url = row[1]
            category = classify_product(product_name)
            writer.writerow([product_name, product_url, category])

# Path to the original and new CSV files
csv_file_path = 'nivea_pages_products.csv'
output_file_path = 'classified_products.csv'

classify_products(csv_file_path, output_file_path)