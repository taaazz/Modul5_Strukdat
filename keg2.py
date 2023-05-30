class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data <= root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print("    " * level + str(node.data))
        print_tree(node.left, level + 1)

def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")

# Main program
root = None

n = int(input("Masukkan jumlah nilai yang akan dimasukkan: "))

for i in range(n):
    data = input("Masukkan nilai ke-%d: " % (i+1))
    root = insert(root, data)

print("\nBinary Tree:")
print_tree(root)

print("\nPreorder Traversal:")
preorder_traversal(root)

print("\nInorder Traversal:")
inorder_traversal(root)

print("\nPostorder Traversal:")
postorder_traversal(root)
