class HashTable:
    class Node:
        # node store a key-value pair and a ptr to the next node
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None  # linked list pointer (for chaining)

    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity  # create the bucket array

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)  # get the bucket index

        # if bucket is empty, place node directly
        if self.table[index] is None:
            self.table[index] = self.Node(key, value)
            self.size += 1
        else:
            # collision occurrs, then traverse chain
            current = self.table[index]
            while current:
                if current.key == key:  # if the same key is found, update the value
                    current.value = value
                    return  # exit the method after updating
                current = current.next  # move to the next item in the chain

            # key not found, insert at the head
            new_node = self.Node(key, value)  # create a new node
            new_node.next = self.table[index]  # let the new node point to the first node
            self.table[index] = new_node  # insert the new node as the first node
            self.size += 1  # increment the count by 1

    def search(self, key):
        index = self._hash(key)

        current = self.table[index]
        # check the linked list in that bucket
        while current:
            if current.key == key:  # if the key is found, this will be true
                return current.value  # return the value if the key is found
            current = current.next  # if the key is not yet found, move to the next item

        return None

    def __len__(self):
        return self.size  # number of key-value pairs stored

    def print_table(self):
        for i in range(self.capacity):
            print(f"{i}: ", end="")
            current = self.table[i]
            first = True
            while current:
                if not first:
                    print(" -> ", end="")  # show chaining
                # show key and value
                print(f"{{ {current.key}: {current.value} }}", end="")
                first = False
                current = current.next
            print("")  # new line for next bucket
