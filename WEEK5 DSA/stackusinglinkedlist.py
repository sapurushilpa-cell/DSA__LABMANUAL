class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        x = int(input("Enter element: "))

        new_node = Node(x)

        new_node.next = self.top
        self.top = new_node

        print("Element pushed")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Deleted element:", self.top.data)
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top

        print("Stack elements:")

        while temp is not None:
            print(temp.data)
            temp = temp.next


s = Stack()

while True:
    print("\n--- STACK USING LINKED LIST ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        s.push()

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")
