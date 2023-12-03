import requests
from product import Product

API_KEY = "169k8tTuaWk4P5o8Z"
API_URL = "https://chompthis.com/api/v2/food/branded/name.php?api_key=" + API_KEY

def getProductData(product_name):
    response = requests.get(API_URL + "&name=" + product_name)
    data = response.json()

    if data['status'] == 404:
        return None

    product = Product(data['name'], data['upc'], data['price'])
    return product