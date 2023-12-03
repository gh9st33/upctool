1. Exported Variables:
   - `API_KEY`: The API key for accessing the ChompThis API, shared across "api_access.py", "main.py", and "web_scraper.py".
   - `PRODUCT_LIST`: A list of product names, shared across "main.py", "product_list.py", "web_scraper.py", and "barcode_generator.py".

2. Data Schemas:
   - `Product`: A data schema representing a product, including its name, UPC, and price. This is shared across "product.py", "web_scraper.py", "api_access.py", and "barcode_generator.py".

3. DOM Element IDs:
   - `product-input`: The input field for entering a product name, used in "interface.py".
   - `product-list`: The list of selected products, used in "interface.py" and "product_list.py".
   - `barcode-display`: The area for displaying generated barcodes, used in "interface.py" and "barcode_generator.py".

4. Message Names:
   - `productSelected`: A message sent when a product is selected, used in "interface.py" and "product_list.py".
   - `barcodeGenerated`: A message sent when a barcode is generated, used in "interface.py" and "barcode_generator.py".

5. Function Names:
   - `getProductData`: A function for retrieving product data from the ChompThis API and the web scrapers, used in "api_access.py", "web_scraper.py", and "main.py".
   - `generateBarcode`: A function for generating a barcode for a product, used in "barcode_generator.py" and "main.py".
   - `addProduct`: A function for adding a product to the list of selected products, used in "product_list.py" and "main.py".
   - `printBarcodes`: A function for printing all selected product barcodes to one page, used in "main.py" and "barcode_generator.py".