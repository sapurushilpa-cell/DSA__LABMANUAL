# Hashing using Separate Chaining, Linear Probing and Quadratic Probing

size = 10

# Separate Chaining
chain = [[] for i in range(size)]

def separate_chaining(key):
    index = key % size
    chain[index].append(key)

# Linear Probing
linear = [None] * size

def linear_probing(key):
    index = key % size

    while linear[index] is not None:
        index = (index + 1) % size

    linear[index] = key

# Quadratic Probing
quadratic = [None] * size

def quadratic_probing(key):
    index = key % size
    i = 0

    while quadratic[(index + i * i) % size] is not None:
        i += 1

        if i == size:
            print("Hash table is full")
            return

    quadratic[(index + i * i) % size] = key


while True:
    print("\n1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Display All")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        key = int(input("Enter key: "))
        separate_chaining(key)
        print("Key inserted successfully")

    elif ch == 2:
        key = int(input("Enter key: "))
        linear_probing(key)
        print("Key inserted successfully")

    elif ch == 3:
        key = int(input("Enter key: "))
        quadratic_probing(key)

    elif ch == 4:
        print("\nSeparate Chaining:", chain)
        print("Linear Probing:", linear)
        print("Quadratic Probing:", quadratic)

    elif ch == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
