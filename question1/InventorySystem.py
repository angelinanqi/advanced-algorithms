from LocalStorage import BabyProduct, inventory


def is_empty_input(prompt, error_message):
    """
    validate input is not empty
    """
    user_input = input(prompt).strip()
    while user_input == '':
        print(error_message)
        user_input = input(prompt).strip()
    return user_input


def show_available_ids():
    """
    display all product IDs in inventory
    """
    ids = []
    for i in range(inventory.capacity):
        current = inventory.table[i]
        while current:
            ids.append(current.key)
            current = current.next
    print("\nAvailable Product IDs:", ids, "\n")


def insert_product():
    """
    insert a new product into the inventory
    """
    print("\n" + "=" * 60)
    print(f"{'INSERT PRODUCT':^60s}")
    print("=" * 60)

    product_id = is_empty_input("Enter product ID: ", "Product ID cannot be empty!")
    name = is_empty_input("Enter product name: ", "Name cannot be empty!")

    price_input = ''
    while True:
        price_input = is_empty_input("Enter product price: ", "Price cannot be empty!")
        try:
            price = float(price_input)
            break
        except ValueError:
            print("Invalid input! Price must be a number.")

    quantity_input = ''
    while True:
        quantity_input = is_empty_input("Enter product quantity: ", "Quantity cannot be empty!")
        if quantity_input.isdigit():
            quantity = int(quantity_input)
            break
        else:
            print("Invalid input! Quantity must be an integer.")

    new_product = BabyProduct(product_id, name, price, quantity)
    inventory.insert(product_id, new_product)
    print("\nProduct inserted successfully!\n")


def search_product():
    """
    search for a product by ID
    """
    print("\n" + "=" * 60)
    print(f"{'SEARCH PRODUCT':^60s}")
    print("=" * 60)

    show_available_ids()
    product_id = is_empty_input("Enter product ID to search: ", "Product ID cannot be empty!")
    product = inventory.search(product_id)
    if product:
        print("\nProduct found:\n", product)
    else:
        print("\nProduct not found.\n")


def edit_product():
    """
    edit an existing product in inventory
    """
    print("\n" + "=" * 60)
    print(f"{'EDIT PRODUCT':^60s}")
    print("=" * 60)

    show_available_ids()
    product_id = is_empty_input("Enter product ID to edit: ", "Product ID cannot be empty!")
    product = inventory.search(product_id)

    if product:
        print("\nCurrent product details:")
        print(product)
        print("Press [Enter] to keep current value.\n")

        name = input("Enter new name: ").strip()
        if name == '':
            name = product.name

        while True:
            price_input = input("Enter new price: ").strip()
            if price_input == '':
                price = product.price
                break
            try:
                price = float(price_input)
                break
            except ValueError:
                print("Invalid input! Price must be a number.")

        while True:
            quantity_input = input("Enter new quantity: ").strip()
            if quantity_input == '':
                quantity = product.quantity
                break
            if quantity_input.isdigit():
                quantity = int(quantity_input)
                break
            else:
                print("Invalid input! Quantity must be an integer.")

        updated_product = BabyProduct(product_id, name, price, quantity)
        inventory.insert(product_id, updated_product)
        print("\nProduct updated successfully!\n")
    else:
        print("\nProduct not found.\n")


def delete_product():
    """
    delete a product from inventory
    """
    print("\n" + "=" * 60)
    print(f"{'DELETE PRODUCT':^60s}")
    print("=" * 60)

    show_available_ids()
    product_id = is_empty_input("Enter product ID to delete: ", "Product ID cannot be empty!")

    index = inventory._hash(product_id)
    current = inventory.table[index]
    previous = None
    found = False

    while current:
        if current.key == product_id:
            if previous:
                previous.next = current.next
            else:
                inventory.table[index] = current.next
            inventory.size -= 1
            found = True
            break
        previous = current
        current = current.next

    if found:
        print("\nProduct deleted successfully!\n")
    else:
        print("\nProduct not found.\n")


def view_inventory():
    """
    display all products in inventory in clean multi-line format
    """
    print("\n" + "=" * 60)
    print(f"{'VIEW INVENTORY':^60s}")
    print("=" * 60)

    for i in range(inventory.capacity):

        current = inventory.table[i]
        while current:
            product = current.value
            print(f"ID       : {product.id}")
            print(f"Name     : {product.name}")
            print(f"Price    : RM{product.price:.2f}")
            print(f"Quantity : {product.quantity}")
            print("-" * 60)
            current = current.next

    print("\n")



def main():
    """
    main menu for inventory system
    """
    choice = 0
    while choice != 6:
        print("\n" + "=" * 60)
        print(f"{'🧸 LITTLE BABY SHOP INVENTORY SYSTEM 🍼':^60s}")
        print("=" * 60)
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. View All Products")
        print("6. Exit")
        print("=" * 60)

        choice_input = is_empty_input("Enter your choice: ", "Choice cannot be empty!")

        if not choice_input.isdigit():
            print("Invalid input! Enter a number from 1-6.")
            continue

        choice = int(choice_input)

        if choice == 1:
            insert_product()
        elif choice == 2:
            search_product()
        elif choice == 3:
            edit_product()
        elif choice == 4:
            delete_product()
        elif choice == 5:
            view_inventory()
        elif choice == 6:
            print("\nExiting inventory system. Goodbye!")
        else:
            print("Invalid choice! Enter a number from 1-6.")


if __name__ == '__main__':
    main()
