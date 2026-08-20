class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlelinkedlist:
    def __init__(self):
        self.head = None
    def insert_begin(self,data):

        new=Node(data)
        new.next=self.head
        self.head=new


    def insert_end(self,data):
        new=Node(data)

        if self.head is None:
            self.head=new

        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new

    def insert_index(self,index,data):
        if index==0:
            self.insert_begin(data)
            return

        elif index>self.count() or index<0:
            print("invalid index")
            return
        new=Node(data)
        temp=self.head
        for i in range(index-1):
            temp=temp.next
            new.temp=temp.next
            temp.next=new
    def delete_begin(self):
        if self.head is None:
            print("data is not deleted")

        else:
            temp=self.head
            self.head=temp.next
            print("deleted value =",temp.data)

    def delete_end(self):
        if self.head is None:
            prinmt("no data is deleted")

        elif self.head.next is None:
            self.head=None

        else:
            temp=self.head
            temp1=temp
            while temp.next:
                temp1=temp
                temp=temp.next
            temp.next=None


    def delete(self,value):
        if self.head is None:
            print("no dta is deleted ")

        else:
            temp=self.head
            if temp and temp.data==value:
                self.head=temp.next
                print("value deleted")
                return

            while temp.next and temp.next.data!=value:
                temp=temp.next

            if temp_next is None:
                print("value is not present")

            else:
                temp.next=temp.next.next

    def count(self):
        if self.head is None:
            print("no linked list")

        else:
            c=0
            temp=self.head
            while temp:
                c+=1
                temp=temp.next

            print(f"Number of nodes in {c}")

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")
        

list1 = Singlelinkedlist()

while True:

    print("\n========== SINGLE LINKED LIST ==========")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Index")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete by Value")
    print("7. Count Nodes")
    print("8. Display List")
    print("9. Search")
    print("10. Exit")
    print("========================================")

    choice = int(input("Enter your choice: "))
    data=list(map(int,input("enter the data").split()))

    if choice == 1:
        data = int(input("Enter data: "))
        list1.insert_begin(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        list1.insert_end(data)

    elif choice == 3:
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))
        list1.insert_index(index, data)

    elif choice == 4:
        list1.delete_begin()

    elif choice == 5:
        list1.delete_end()

    elif choice == 6:
        value = int(input("Enter value to delete: "))
        list1.delete(value)

    elif choice == 7:
        print("Number of nodes =", list1.count())

    elif choice == 8:
        list1.display()

    elif choice == 9:
        value = int(input("Enter value to search: "))
        list1.search(value)

    elif choice == 10:
        list1.exit_program()
        break

    else:
        print("Invalid choice")

            





        
    
        
