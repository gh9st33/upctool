```python
import requests
import json

def send_get_request(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def send_post_request(url, data, headers=None):
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def parse_product_data(data):
    try:
        product_name = data['name']
        product_upc = data['upc']
        product_price = data['price']
        return product_name, product_upc, product_price
    except KeyError as err:
        print(f'Key error: {err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def generate_barcode(upc):
    try:
        barcode = '*'+str(upc)+'*'
        return barcode
    except Exception as err:
        print(f'Error occurred while generating barcode: {err}')
```