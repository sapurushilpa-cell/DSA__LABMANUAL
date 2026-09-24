class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # a. Create a linked list
    def create(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

        print("Node created successfully")

    # b. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node
        print("Node inserted at beginning")

    # c. Insert at end
    def insert_end(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

        print("Node inserted at end")

    # d. Insert at a specific index
    def insert_index(self):
        data = int(input("Enter the data: "))
        index = int(input("Enter the index: "))

        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            new_node = Node(data)
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            print("Node inserted successfully")
            return

        temp = self.head
        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print("Node inserted successfully")

    # e. Delete by value
    def delete_value(self):
        value = int(input("Enter the value to delete: "))
        temp = self.head

        while temp is not None:
            if temp.data == value:

                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next is not None:
                    temp.next.prev = temp.prev

                print("Node deleted successfully")
                return

            temp = temp.next

        print("Value not found")

    # f. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print("First node deleted")

    # g. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        if temp.prev is None:
            self.head = None
        else:
            temp.prev.next = None

        print("Last node deleted")

    # h. Count number of nodes
    def count(self):
        temp = self.head
        count = 0

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # i. Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        print("Doubly Linked List:")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main program
dll = DoublyLinkedList()

while True:
    print("\n--- DOUBLY LINKED LIST MENU ---")
    print("1. Create a linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dll.create()

    elif choice == 2:
        dll.insert_beginning()

    elif choice == 3:
        dll.insert_end()

    elif choice == 4:
        dll.insert_index()

    elif choice == 5:
        dll.delete_value()

    elif choice == 6:
        dll.delete_first()

    elif choice == 7:
        dll.delete_last()

    elif choice == 8:
        dll.count()

    elif choice == 9:
        dll.display()

    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
