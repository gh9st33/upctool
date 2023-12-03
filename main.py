```python
import api_access
import web_scraper
import product
import barcode_generator
import interface
import product_list
import utils
import config

API_KEY = config.API_KEY
PRODUCT_LIST = []

def main():
    interface.init()

    while True:
        event, values = interface.get_event()

        if event == "productSelected":
            product_name = values["product-input"]
            product_data = getProductData(product_name)
            if product_data:
                addProduct(product_data)
                interface.update_product_list(PRODUCT_LIST)

        elif event == "barcodeGenerated":
            product_name = values["product-list"]
            product_data = next((p for p in PRODUCT_LIST if p.name == product_name), None)
            if product_data:
                barcode = generateBarcode(product_data)
                interface.display_barcode(barcode)

        elif event == "printBarcodes":
            printBarcodes(PRODUCT_LIST)

def getProductData(product_name):
    product_data = api_access.get_product_data(API_KEY, product_name)
    if not product_data:
        product_data = web_scraper.get_product_data(product_name)
    return product_data

def addProduct(product_data):
    new_product = product.Product(product_data["name"], product_data["upc"], product_data["price"])
    PRODUCT_LIST.append(new_product)

def generateBarcode(product):
    return barcode_generator.generate(product.upc)

def printBarcodes(product_list):
    barcodes = [generateBarcode(p) for p in product_list]
    utils.print_to_page(barcodes)

if __name__ == "__main__":
    main()
```