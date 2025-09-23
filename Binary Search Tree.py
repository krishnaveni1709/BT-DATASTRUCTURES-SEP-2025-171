class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.data:
        root.left = insert(root.left, val)
    elif val > root.data:
        root.right = insert(root.right, val)
    return root
def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
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
def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current
def delete_node(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    return root
def update_node(root, old_val, new_val):
    root = delete_node(root, old_val)
    root = insert(root, new_val)
    return root
arr = [8, 3, 10, 1, 6, 14, 4, 7]
root = None
for val in arr:
    root = insert(root, val)

print("Inorder traversal:", end=" ")
inorder(root)
print()

print("Preorder traversal:", end=" ")
preorder(root)
print()

print("Postorder traversal:", end=" ")
postorder(root)
print()

print("Search for 10:", search(root, 10))
print("Search for 20:", search(root, 20))

root = delete_node(root, 6)
print("Inorder traversal after deleting 6:", end=" ")
inorder(root)
print()

root = update_node(root, 3, 5)
print("Inorder traversal after updating 3 to 5:", end=" ")
inorder(root)
print()
                                     
