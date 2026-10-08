class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def search(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    if data < root.data:
        return search(root.left, data)

    return search(root.right, data)


def minimum(root):
    while root.left:
        root = root.left
    return root.data


def maximum(root):
    while root.right:
        root = root.right
    return root.data


def delete(root, data):
    if root is None:
        return None

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def count(root):
    if root is None:
        return 0

    return 1 + count(root.left) + count(root.right)


root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    x = int(input("Enter value: "))
    root = insert(root, x)

print("Inorder:", end=" ")
inorder(root)

print("\nPreorder:", end=" ")
preorder(root)

print("\nPostorder:", end=" ")
postorder(root)

print("\nSearch 40:", search(root, 40))
print("Minimum:", minimum(root))
print("Maximum:", maximum(root))
print("Height:", height(root))
print("Count:", count(root))

root = delete(root, 40)

print("After delete:", end=" ")
inorder(root)
