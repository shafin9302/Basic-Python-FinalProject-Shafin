class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

inventory = {}

def add_product():
    global inventory
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter initial quantity: "))
    inventory[name] = {'price': price, 'quantity': quantity}
    print(f"{name} added to inventory.")

def update_product():
    global inventory
    product_name = input("Enter product name: ")
    action = input("Enter action (buy/sell/delete): ").lower()
    amount = int(input("Enter amount: "))

    if product_name in inventory:
        if action == "buy":
            inventory[product_name]["quantity"] += amount
        elif action == "sell":
            if inventory[product_name]["quantity"] >= amount:
                inventory[product_name]["quantity"] -= amount
            else:
                print(f"Not enough stock of {product_name} to sell.")
        elif action == "delete":
            del inventory[product_name]
            print(f"{product_name} deleted from inventory.")
    else:
        print(f"{product_name} not found in inventory.")

def print_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for product_name, product_details in inventory.items():
            print(f"{product_name}: Price: {product_details['price']}, Quantity: {product_details['quantity']}")

def save_inventory():
    try:
        with open("inventory.txt", "w") as f:
            for product_name, product_details in inventory.items():
                f.write(f"{product_name},{product_details['price']},{product_details['quantity']}\n")
        print("Inventory saved to file.")
    except Exception as e:
        print(f"Error saving inventory: {e}")

while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Update Product (Buy/Sell/Delete)")
    print("3. View Inventory")
    print("4. Save Inventory")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_product()
    elif choice == '2':
        update_product()
    elif choice == '3':
        print_inventory()
    elif choice == '4':
        save_inventory()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
