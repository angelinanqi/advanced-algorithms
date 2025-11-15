from HashTable import HashTable

class BabyProduct:
    def __init__(self, id, name, price, quantity):
        """
        :param id: id in the format of A00X. (string to support hash function)
        :param name: product name. (string)
        :param price: price of the product (float)
        :param quantity: how many of the products are in the inventory (int)
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Name: {self.name} | ID: {self.id} | Price: RM{self.price:.2f} | Quantity: {self.quantity}"


# initialize inventory
inventory = HashTable(20)

# preload some products
products = [
    BabyProduct("A001", "Baby Hat", 8.0, 50),
    BabyProduct("A002", "Baby Shirt", 28.0, 40),
    BabyProduct("A003", "Baby Pants", 28.0, 35),
    BabyProduct("A004", "Baby Onesie", 40.0, 60),
    BabyProduct("A005", "Baby Socks", 12.0, 100),
    BabyProduct("A006", "Baby Shoes", 20.0, 25),
    BabyProduct("A007", "Teddy Bear", 25.0, 30),
    BabyProduct("A008", "Baby Oil", 12.0, 40),
    BabyProduct("A009", "Rattle Toy", 7.0, 50),
    BabyProduct("A010", "Baby Powder", 10.0, 35)
]

for product in products:
    inventory.insert(product.id, product)

# test search
if __name__ == '__main__':
    product1 = inventory.search("A011")
    product2 = inventory.search("A004")

    if product1:
        print("Product 1 found:\n", product1)
    else:
        print("Product 1 not found.")

    if product2:
        print("Product 2 found:\n", product2)
    else:
        print("Product 2 not found.")

    print("\n=================")
    print("Current Inventory")
    print("=================")
    inventory.print_table()
