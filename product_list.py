```python
from product import Product

class ProductList:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("Only Product instances can be added to the product list.")

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def get_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def get_all_products(self):
        return self.products
```