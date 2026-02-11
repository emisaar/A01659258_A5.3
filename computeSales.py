import json
import os, sys
import time


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_price_catalogue(products):
    catalogue = {}
    for product in products:
        title = product.get("title")
        price = product.get("price")
        if title is None or price is None:
            print(f"Warning: Invalid product entry skipped: {product}")
            continue
        catalogue[title] = price
    return catalogue

def compute_sales(catalogue, sales):
    total = 0.0
    for sale in sales:
        product_name = sale.get("Product")
        quantity = sale.get("Quantity")

        if product_name is None or quantity is None:
            print(f"Error: Missing data in sale record: {sale}")
            continue

        if not isinstance(quantity, (int, float)):
            print(f"Error: Invalid quantity ({quantity}) for product '{product_name}' in SALE_ID {sale.get('SALE_ID')}. Skipping.")
            continue

        if product_name not in catalogue:
            print(f"Error: Product '{product_name}' not found in catalogue. SALE_ID {sale.get('SALE_ID')}. Skipping.")
            continue

        total += catalogue[product_name] * quantity

    return total

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    start_time = time.time()

    try:
        products = load_json(catalogue_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading catalogue file: {e}")
        sys.exit(1)

    try:
        sales = load_json(sales_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading sales file: {e}")
        sys.exit(1)

    catalogue = build_price_catalogue(products)
    total = compute_sales(catalogue, sales)

    elapsed = time.time() - start_time

    sales_name = os.path.basename(sales_file)
    result_lines = [
        f"--- {sales_name} ---",
        f"Total sales cost: ${total:,.2f}",
        f"Time elapsed: {elapsed:.4f} seconds",
        "",
    ]

    for line in result_lines:
        print(line)

    os.makedirs("results", exist_ok=True)
    output_path = os.path.join("results", "SalesResults.txt")
    with open(output_path, 'a', encoding='utf-8') as f:
        for line in result_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
