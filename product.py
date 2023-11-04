```python
class Product:
    def __init__(self, name, upc, price):
        self.name = name
        self.upc = upc
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, upc={self.upc}, price={self.price})"

    def __repr__(self):
        return self.__str__()
```