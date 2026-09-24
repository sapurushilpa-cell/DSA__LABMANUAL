class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # a. Create a linked list
    def create(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        print("Node created successfully")

    # b. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

        print("Node inserted at beginning")

    # c. Insert at end
    def insert_end(self):
        data = int(input("Enter the data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

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

            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head

            print("Node inserted successfully")
            return

        if self.head is None:
            print("Invalid index")
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid index")
                return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

        if temp == self.tail:
            self.tail = new_node

        print("Node inserted successfully")

    # e. Delete by value
    def delete_value(self):
        value = int(input("Enter the value to delete: "))

        if self.head is None:
            print("List is empty")
            return

        current = self.head
        previous = self.tail

        while True:
            if current.data == value:

                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                else:
                    previous.next = current.next

                    if current == self.head:
                        self.head = current.next

                    if current == self.tail:
                        self.tail = previous

                    self.tail.next = self.head

                print("Node deleted successfully")
                return

            previous = current
            current = current.next

            if current == self.head:
                break

        print("Value not found")

    # f. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        print("First node deleted")

    # g. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head

            while temp.next != self.tail:
                temp = temp.next

            temp.next = self.head
            self.tail = temp

        print("Last node deleted")

    # h. Count number of nodes
    def count(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    # i. Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        print("Circular Linked List:")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("HEAD")

    # j. Display head and tail
    def display_head_tail(self):
        if self.head is None:
            print("List is empty")
            return

        print("Head:", self.head.data)
        print("Tail:", self.tail.data)

    # k. Print data from tail to head
    def print_tail_to_head(self):
        if self.head is None:
            print("List is empty")
            return

        values = []
        temp = self.head

        while True:
            values.append(temp.data)
            temp = temp.next

            if temp == self.head:
                break

        print("Data from tail to head:")

        for data in reversed(values):
            print(data, end=" -> ")

        print("HEAD")


# Main program
cll = CircularLinkedList()

while True:
    print("\n--- CIRCULAR LINKED LIST MENU ---")
    print("1. Create a linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display")
    print("10. Display head and tail")
    print("11. Print data from tail to head")
    print("12. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        cll.insert_beginning()

    elif choice == 3:
        cll.insert_end()

    elif choice == 4:
        cll.insert_index()

    elif choice == 5:
        cll.delete_value()

    elif choice == 6:
        cll.delete_first()

    elif choice == 7:
        cll.delete_last()

    elif choice == 8:
        cll.count()

    elif choice == 9:
        cll.display()

    elif choice == 10:
        cll.display_head_tail()

    elif choice == 11:
        cll.print_tail_to_head()

    elif choice == 12:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
