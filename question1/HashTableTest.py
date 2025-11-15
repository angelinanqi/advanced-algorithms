import time
from LocalStorage import inventory, products, BabyProduct

def main():
    # copy the objects from inventory (LocalStorage) into a list (1d array)
    inventory_list = list(products)

    start_time = 0
    end_time = 0
    hash_time = 0
    array_time = 0

    # get all product ids
    all_ids = [product.id for product in inventory_list]

    # ======================================test on original products (10)===================================================================

    # hash table search for original inventory
    start_time = time.time()  # start timing
    for pid in all_ids:
        product = inventory.search(pid)
        if product:
            pass  # found, do nothing
    hash_time = time.time() - start_time
    print(f"original inventory - hash table search time: {hash_time:.8f} seconds")

    # 1d array search for original inventory
    start_time = time.time()  # start timing
    for pid in all_ids:
        for product in inventory_list:
            if product.id == pid:  # make sure there is a product
                break  # found it, move to next pid
    array_time = time.time() - start_time
    print(f"original inventory - array search time: {array_time:.8f} seconds")

    if hash_time < array_time:
        print("original inventory - hash table search is faster.\n")
    elif array_time < hash_time:
        print("original inventory - array search is faster.\n")
    else:
        print("original inventory - hash table and array search took the same time.\n")

    # ======================================test on larger amount of item (100)===================================================================
    # add 100 more products (A011 to A110)
    for i in range(11, 111):
        pid = f"a{i:03d}"  # create id like a011; 03 mean 3 digit
        new_product = BabyProduct(pid, "product", 1.0, 1)  # make extra test products to test on bigger size
        products.append(new_product)
        inventory.insert(new_product.id, new_product)

    # copy large inventory into a list
    inventory_list_large = list(products)
    all_ids_large = [product.id for product in inventory_list_large]

    # hash table search for large inventory
    start_time = time.time()  # start timing
    for pid in all_ids_large:
        product = inventory.search(pid)
        if product:
            pass  # found, do nothing
    hash_time_large = time.time() - start_time
    print(f"large inventory - hash table search time: {hash_time_large:.8f} seconds")

    # 1d array search for large inventory
    start_time = time.time()  # start timing
    for pid in all_ids_large:
        for product in inventory_list_large:
            if product.id == pid:
                break  # found it, move to next pid
    array_time_large = time.time() - start_time
    print(f"large inventory - array search time: {array_time_large:.8f} seconds")

    # performance comparison
    if hash_time_large < array_time_large:
        print("large inventory - hash table search is faster.")
    elif array_time_large < hash_time_large:
        print("large inventory - array search is faster.")
    else:
        print("large inventory - hash table and array search took the same time.")


if __name__ == '__main__':
    main()
