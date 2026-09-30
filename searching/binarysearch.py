class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.right = Node(80)

result = []
inorder(root, result)
print("Inorder traversal:", result)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(node, target):
    if node is None:
        return False
    if node.data == target:
        return True
    if target < node.data:
        return search(node.left, target)
    return search(node.right, target)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

print("Searching for 40:", "found" if search(root, 40) else "not found")
print("Searching for 45:", "found" if search(root, 45) else "not found")


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    return node


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


root = None
for value in [50, 30, 70, 20, 40, 35]:
    root = insert(root, value)

result = []
inorder(root, result)
print("Inorder after insertion:", result)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    return node


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def delete_node(node, value):
    if node is None:
        return None

    if value < node.data:
        node.left = delete_node(node.left, value)
    elif value > node.data:
        node.right = delete_node(node.right, value)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        successor = find_min(node.right)
        node.data = successor.data
        node.right = delete_node(node.right, successor.data)

    return node


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


root = None
for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)

root = delete_node(root, 30)

result = []
inorder(root, result)
print("Inorder after deleting 30:", result)


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def find_successor(node):
    if node.right is not None:
        return find_min(node.right)
    ancestor = node.parent
    while ancestor is not None and node == ancestor.right:
        node = ancestor
        ancestor = ancestor.parent
    return ancestor


root = Node(50)
root.left = Node(30, root)
root.right = Node(70, root)
root.left.left = Node(20, root.left)
root.left.right = Node(40, root.left)

successor_of_30 = find_successor(root.left)
print("Successor of 30:", successor_of_30.data)

successor_of_40 = find_successor(root.left.right)
print("Successor of 40:", successor_of_40.data)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True

    if node.data <= min_val or node.data >= max_val:
        return False

    return (is_valid_bst(node.left, min_val, node.data) and
            is_valid_bst(node.right, node.data, max_val))


invalid_tree = Node(50)
invalid_tree.left = Node(30)
invalid_tree.left.right = Node(60)

valid_tree = Node(50)
valid_tree.left = Node(30)
valid_tree.right = Node(70)

print("Invalid tree check:", "valid" if is_valid_bst(invalid_tree) else "invalid")
print("Valid tree check:", "valid" if is_valid_bst(valid_tree) else "invalid")



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    return node


def find_lca(node, target1, target2):
    while node is not None:
        if target1 < node.data and target2 < node.data:
            node = node.left
        elif target1 > node.data and target2 > node.data:
            node = node.right
        else:
            return node
    return None


root = None
for value in [50, 30, 70, 20, 40]:
    root = insert(root, value)

lca1 = find_lca(root, 20, 40)
print("LCA of 20 and 40:", lca1.data)

lca2 = find_lca(root, 20, 70)
print("LCA of 20 and 70:", lca2.data)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    return node


def find_lca(node, target1, target2):
    while node is not None:
        if target1 < node.data and target2 < node.data:
            node = node.left
        elif target1 > node.data and target2 > node.data:
            node = node.right
        else:
            return node
    return None


root = None
for value in [50, 30, 70, 20, 40]:
    root = insert(root, value)

lca1 = find_lca(root, 20, 40)
print("LCA of 20 and 40:", lca1.data)

lca2 = find_lca(root, 20, 70)
print("LCA of 20 and 70:", lca2.data)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    return node


def find_lca(node, target1, target2):
    while node is not None:
        if target1 < node.data and target2 < node.data:
            node = node.left
        elif target1 > node.data and target2 > node.data:
            node = node.right
        else:
            return node
    return None


root = None
for value in [50, 30, 70, 20, 40]:
    root = insert(root, value)

lca1 = find_lca(root, 20, 40)
print("LCA of 20 and 40:", lca1.data)

lca2 = find_lca(root, 20, 70)
print("LCA of 20 and 70:", lca2.data)






