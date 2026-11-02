class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key):
        index = key % self.size
        new_node = Node(key)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            temp = self.table[index]

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

        print("Key inserted successfully")

    def search(self, key):
        index = key % self.size
        temp = self.table[index]

        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    def display(self):
        for i in range(self.size):
            print(i, end=": ")
            temp = self.table[i]

            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")


ht = HashTable(10)

while True:
    print("\n--- HASHING USING LINKED LIST ---")
    print("1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        key = int(input("Enter key: "))
        ht.insert(key)

    elif ch == 2:
        key = int(input("Enter key to search: "))

        if ht.search(key):
            print("Key found")
        else:
            print("Key not found")

    elif ch == 3:
        ht.display()

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
