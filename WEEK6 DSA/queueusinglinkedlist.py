class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self):
        x=int(input("enter element"))
        
        new_node=Node(x)
        
        if self.rear is None:
            
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
            
        print("element inserted")
        
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            print("Deleted element:", self.front.data)

            self.front = self.front.next

            if self.front is None:
                self.rear = None

    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Queue elements:")

            temp = self.front

            while temp is not None:
                print(temp.data)
                temp = temp.next


q = Queue()

while True:
    print("\n--- QUEUE USING LINKED LIST ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        q.enqueue()

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")
            
    