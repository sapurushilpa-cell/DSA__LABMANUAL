class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
        
    def enqueue(self):
        if self.rear==self.size-1:
            print("Overflow")
            
        else:
            x=int(input("enter element"))
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.queue[self.rear]=x
            print("element inserted")
            
    def dequeue(self):
        if self.front==-1 or self.front>self.rear:
            
            print("queue is underflow")
            
        else:
            print("Deleted element:", self.queue[self.front])
            self.queue[self.front] = None
            self.front += 1

            if self.front > self.rear:
                self.front = -1
                self.rear = -1
    def peek(self):
        if self.front==-1:
            print("queue is empty")
            
        else:
            print("front element:",self.queue[self.front])
            
    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Queue elements:")

            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


size = int(input("Enter queue size: "))

q = Queue(size)

while True:
    print("\n--- QUEUE USING ARRAY ---")
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