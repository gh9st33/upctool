import tkinter as tk
from tkinter import messagebox
import product_list
import main

class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("UPC and Price Finder")
        self.create_widgets()

    def create_widgets(self):
        self.product_input = tk.Entry(self.window, width=50)
        self.product_input.pack()
        self.product_input.bind('<Return>', self.add_product)

        self.product_list = tk.Listbox(self.window)
        self.product_list.pack()

        self.generate_button = tk.Button(self.window, text="Generate Barcodes", command=self.generate_barcodes)
        self.generate_button.pack()

        self.barcode_display = tk.Canvas(self.window)
        self.barcode_display.pack()

    def add_product(self, event):
        product_name = self.product_input.get()
        if product_name:
            product = main.getProductData(product_name)
            if product:
                product_list.addProduct(product)
                self.product_list.insert(tk.END, product.name)
            else:
                messagebox.showerror("Error", "Product not found")
            self.product_input.delete(0, tk.END)

    def generate_barcodes(self):
        products = product_list.PRODUCT_LIST
        for product in products:
            barcode = main.generateBarcode(product)
            if barcode:
                self.barcode_display.create_image(10, 10, image=barcode, anchor='nw')
            else:
                messagebox.showerror("Error", f"Could not generate barcode for {product.name}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Interface()
    app.run()