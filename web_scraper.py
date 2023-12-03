```python
import requests
from bs4 import BeautifulSoup
from product import Product

API_KEY = "169k8tTuaWk4P5o8Z"

def scrape_target(product_name):
    url = f"https://www.target.com/s?searchTerm={product_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    product_data = soup.find('div', {'data-test': 'product-price'}).text
    price, upc = product_data.split('|')
    return Product(product_name, upc.strip(), price.strip())

def scrape_kroger(product_name):
    url = f"https://www.kroger.com/search?query={product_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    product_data = soup.find('div', {'class': 'ProductCard-Price'}).text
    price, upc = product_data.split('|')
    return Product(product_name, upc.strip(), price.strip())

def get_product_data(product_name):
    target_product = scrape_target(product_name)
    kroger_product = scrape_kroger(product_name)
    if target_product.price < kroger_product.price:
        return target_product
    else:
        return kroger_product
```