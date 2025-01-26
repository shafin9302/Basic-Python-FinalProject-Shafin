class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, stock_count, price):
        self.inventory[item_name] = {"stock_count": stock_count, "price": price}

    def update_item(self, item_name, stock_count, price):
        if item_name in self.inventory:
            self.inventory[item_name]["stock_count"] = stock_count
            self.inventory[item_name]["price"] = price
        else:
            print("Item not found in inventory.")

    def check_item_details(self, item_name):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            return f"Product Name: {item['item_name']}, Stock Count: {item['stock_count']}, Price: {item['price']}"
        else:
            return "Item not found in inventory."
