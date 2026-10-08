class BinaryTree:
    def __init__(self, n):
        self.tree = [None] * n

    def insert(self, i, data):
        if i < len(self.tree):
            self.tree[i] = data

    def inorder(self, i):
        if i >= len(self.tree) or self.tree[i] is None:
            return

        self.inorder(2 * i + 1)
        print(self.tree[i], end=" ")
        self.inorder(2 * i + 2)

    def preorder(self, i):
        if i >= len(self.tree) or self.tree[i] is None:
            return

        print(self.tree[i], end=" ")
        self.preorder(2 * i + 1)
        self.preorder(2 * i + 2)

    def postorder(self, i):
        if i >= len(self.tree) or self.tree[i] is None:
            return

        self.postorder(2 * i + 1)
        self.postorder(2 * i + 2)
        print(self.tree[i], end=" ")

    def level_order(self):
        for i in range(len(self.tree)):
            if self.tree[i] is not None:
                print(self.tree[i], end=" ")

    def search(self, data):
        for i in range(len(self.tree)):
            if self.tree[i] == data:
                return i
        return -1

    def count_nodes(self):
        count = 0

        for value in self.tree:
            if value is not None:
                count += 1

        return count

    def find_min(self):
        values = [x for x in self.tree if x is not None]

        if not values:
            return None

        return min(values)

    def find_max(self):
        values = [x for x in self.tree if x is not None]

        if not values:
            return None

        return max(values)

    def height(self, i=0):
        if i >= len(self.tree) or self.tree[i] is None:
            return 0

        left = self.height(2 * i + 1)
        right = self.height(2 * i + 2)

        return 1 + max(left, right)

    def delete(self, data):
        index = self.search(data)

        if index == -1:
            print("Element not found")
        else:
            self.tree[index] = None
            print("Element deleted")


n = int(input("Enter size of tree: "))

bt = BinaryTree(n)

print("Enter elements:")
print("Enter -1 for empty position")

for i in range(n):
    data = int(input(f"Enter element at index {i}: "))

    if data != -1:
        bt.insert(i, data)

print("\nTree:", bt.tree)

print("\nInorder:")
bt.inorder(0)

print("\nPreorder:")
bt.preorder(0)

print("\nPostorder:")
bt.postorder(0)

print("\nLevel Order:")
bt.level_order()

value = int(input("\n\nEnter element to search: "))

result = bt.search(value)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

print("Minimum:", bt.find_min())
print("Maximum:", bt.find_max())
print("Number of nodes:", bt.count_nodes())
print("Height:", bt.height())

value = int(input("\nEnter element to delete: "))
bt.delete(value)

print("Tree after deletion:", bt.tree)

print("Inorder after deletion:")
bt.inorder(0)
