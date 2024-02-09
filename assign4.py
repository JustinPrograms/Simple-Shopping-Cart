"""
All variables and function naming is done using snake case.
This program acts as a maintain electronic shopping carts for customers of multiple vendors.
"""


class Product:
    def __init__(self, name, price, category):
        # Initialize product attributes
        self._name = name
        self._price = price
        self._category = category

    # Define how products are classified
    def __eq__(self, other):
        # Check if two products are equal
        if isinstance(other, Product):
            if ((self._name == other._name and self._price == other._price) and (self._category == other._category)):
                return True
            else:
                return False
        else:
            return False

    def get_name(self):
        # Get the name of the product
        return self._name

    def get_price(self):
        # Get the price of the product as an integer
        return int(self._price)

    def get_category(self):
        # Get the category of the product
        return self._category

    # Implement string representation
    def __repr__(self):
        # Return a string representation of the product
        rep = 'Product(' + self._name + ',' + str(self._price) + ',' + self._category + ')'
        return rep


class Inventory:
    def __init__(self):
        # Initialize an empty dictionary to store inventory items
        self.items = {}

    def add_to_productInventory(self, productName, productPrice, productQuantity):
        # Add or update product quantity in the inventory
        # Parameters: productName (str), productPrice (float), productQuantity (int)
        if productName in self.items:
            # If it exists, update the quantity
            self.items[productName]['quantity'] += productQuantity
        else:
            # If it doesn't exist, add a new entry to the inventory
            self.items[productName] = {'price': productPrice, 'quantity': productQuantity}

    def add_productQuantity(self, nameProduct, addQuantity):
        # Add quantity to a product in the inventory
        # Parameters: nameProduct (str), addQuantity (int)
        self.items[nameProduct]['quantity'] += addQuantity

    def remove_productQuantity(self, nameProduct, removeQuantity):
        # Remove quantity from a product in the inventory
        # Parameters: nameProduct (str), removeQuantity (int)
        if self.items[nameProduct]['quantity'] >= removeQuantity:
            self.items[nameProduct]['quantity'] -= removeQuantity
            return True
        return False

    def get_productPrice(self, nameProduct):
        # Get the price of a product in the inventory
        # Parameters: nameProduct (str)
        return self.items[nameProduct]['price']

    def get_productQuantity(self, nameProduct):
        # Get the quantity of a product in the inventory
        # Parameters: nameProduct (str)
        return self.items[nameProduct]['quantity']

    def display_Inventory(self):
        # Display the contents of the inventory
        for productName, details in self.items.items():
            print(f"{productName}, {int(details['price'])}, {details['quantity']}")


class ShoppingCart:
    def __init__(self, buyerName, inventory):
        # Initialize the shopping cart with the buyer's name and the provided inventory
        # Parameters: buyerName (str), inventory (Inventory)
        self.buyer_name = buyerName
        self.cart_items = {}
        self.inventory = inventory

    def add_to_cart(self, nameProduct, requestedQuantity):
        # Add a product to the shopping cart
        # Parameters: nameProduct (str), requestedQuantity (int)
        if self.inventory.remove_productQuantity(nameProduct, requestedQuantity):
            # Check if the product already exists in the cart
            if nameProduct in self.cart_items:
                # If it exists, update the quantity
                self.cart_items[nameProduct]['quantity'] += requestedQuantity
            else:
                # If it doesn't exist, add a new entry to the cart
                self.cart_items[nameProduct] = {'quantity': requestedQuantity}
            return "Filled the order"
        return "Can not fill the order"

    def remove_from_cart(self, nameProduct, requestedQuantity):
        # Remove a product from the shopping cart
        # Parameters: nameProduct (str), requestedQuantity (int)
        # Returns a message indicating the success or failure of the operation
        if nameProduct not in self.cart_items:
            return "Product not in the cart"

        if requestedQuantity > self.cart_items[nameProduct]['quantity']:
            return "The requested quantity to be removed from cart exceeds what is in the cart"

        self.inventory.add_productQuantity(nameProduct, requestedQuantity)
        self.cart_items[nameProduct]['quantity'] -= requestedQuantity

        if self.cart_items[nameProduct]['quantity'] == 0:
            del self.cart_items[nameProduct]

        return "Successful"

    def view_cart(self):
        # Display the contents of the shopping cart, total price, and buyer name
        total_price = 0
        for product_name, details in self.cart_items.items():
            price_per_item = self.inventory.get_productPrice(product_name)
            quantity = details['quantity']
            total_price += price_per_item * quantity
            print(f"{product_name} {quantity}")

        print(f"Total: {int(total_price)}")
        print(f"Buyer Name: {self.buyer_name}")


class Catalog:
    def __init__(self):
        # Initialize data structures
        self.products = []
        self.low_prices = set()
        self.medium_prices = set()
        self.high_prices = set()

    def add_product(self, product):
        # Add a product to the catalog
        # Parameter: product (Product)
        self.products.append(product)
        # Place the product in the appropriate price category set
        if 0 <= product.get_price() <= 99:
            self.low_prices.add(product.get_name())
        elif 100 <= product.get_price() <= 499:
            self.medium_prices.add(product.get_name())
        elif product.get_price() >= 500:
            self.high_prices.add(product.get_name())

    def price_category(self):
        # Display the number of items in each price category
        print(f"Number of low price items: {len(self.low_prices)}")
        print(f"Number of medium price items: {len(self.medium_prices)}")
        print(f"Number of high price items: {len(self.high_prices)}")

    def display_catalog(self):
        # Display the catalog entries in the order they were added
        for product in self.products:
            print(f"Product: {product.get_name()} Price: {product.get_price()} Category: {product.get_category()}")

# Function to populate inventory
def populate_inventory(filename):


    # Create an instance of the Inventory class
    inventory = Inventory()

    try:
        with open(filename, 'rt') as file:
            for line in file:
                # Split the line into fields
                fields = line.strip().split(',')
                if len(fields) == 4:
                    # Extract fields and convert to appropriate types
                    product_name, price, quantity, category = fields
                    price = float(price)
                    quantity = int(quantity)

                    # Add product to the inventory
                    inventory.add_to_productInventory(product_name, price, quantity)

    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"File not found: {filename}")

    except Exception as e:
        # Handle other exceptions during file reading
        print(f"Error reading file: {e}")

    return inventory

# Function to populate catalog
def populate_catalog(filename):
    # Create an instance of the Catalog class
    catalog = Catalog()

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line into fields
                fields = line.strip().split(',')
                if len(fields) == 4:
                    # Extract fields and convert to appropriate types
                    product_name, price, _, category = fields
                    price = float(price)

                    # Create a Product object
                    product = Product(product_name, price, category)

                    # Add product to the catalog
                    catalog.add_product(product)

    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"File not found: {filename}")

    except Exception as e:
        # Handle other exceptions during file reading
        print(f"Error reading file: {e}")

    return catalog
