class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            x = int(input("Enter element: "))
            self.top += 1
            self.stack[self.top] = x
            print("Element pushed")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print("Deleted element:", self.stack[self.top])
            self.stack[self.top] = None
            self.top -= 1

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[self.top])

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack elements:")

            for i in range(self.top, -1, -1):
                print(self.stack[i])


size = int(input("Enter stack size: "))

s = Stack(size)

while True:
    print("\n--- STACK USING ARRAY ---")
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
