from assign4 import *

# Create and populate an inventory object
inv = populate_inventory("inventory.csv")

# Create and populate a product catalog object
cat = populate_catalog("inventory.csv")

# Make a shopping cart for the current inventory
cart = ShoppingCart("Joe Bloggs", inv)

# Output the current inventory
print("Current Inventory:")
inv.display_Inventory()

# Output the current product catalog
print("\nCurrent Catalog:")
cat.display_catalog()

# Call price_category()
print("\nPrice Category:")
cat.price_category()

# Add some products to the cart:
print("\nAdding products to cart:")
print(cart.add_to_cart("Backpack", 1))
print(cart.add_to_cart("Intro to Python", 10))
print(cart.add_to_cart("Backpack", 1))

# Output the current cart:
print("\nCurrent cart:")
cart.view_cart()

# Output the current inventory
print("\nCurrent Inventory:")
inv.display_Inventory()

# Remove some products from the cart:
print("\nRemoving products from cart:")
print(cart.remove_from_cart("Backpack", 1))
print(cart.remove_from_cart("Intro to Python", 5))
print(cart.remove_from_cart("Intro to Python", 5))

# Output the current cart:
print("\nCurrent cart:")
cart.view_cart()

# Output the current inventory
print("\nCurrent Inventory:")
inv.display_Inventory()