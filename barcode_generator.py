import barcode
from barcode.writer import ImageWriter
from product import Product

def generateBarcode(product: Product):
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(product.upc, writer=ImageWriter())
    filename = f"{product.name.replace(' ', '_')}_barcode"
    ean.save(filename)
    return filename

def printBarcodes(product_list):
    for product in product_list:
        generateBarcode(product)