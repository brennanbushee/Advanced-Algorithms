class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# def build_bst_from_preorder(preorder):
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree_from_inorder_preorder(preorder, inorder):
    def helper(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right:
            return None

        root_value = preorder[pre_left]
        root = BinaryTreeNode(root_value)

        # Find the index of the root value in the inorder list
        root_index_inorder = inorder_index_map[root_value]

        # Calculate the size of the left subtree
        left_subtree_size = root_index_inorder - in_left

        # Recursively build the left and right subtrees
        root.left = helper(pre_left + 1, pre_left + left_subtree_size, in_left, root_index_inorder - 1)
        root.right = helper(pre_left + left_subtree_size + 1, pre_right, root_index_inorder + 1, in_right)

        return root

    # Create a map to quickly find the index of any element in the inorder list
    inorder_index_map = {value: idx for idx, value in enumerate(inorder)}

    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

# Example usage
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = build_tree_from_inorder_preorder(preorder, inorder)

# Function to print the tree in inorder traversal to verify correctness
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.value, end=' ')
        print_inorder(node.right)

print("Inorder traversal of reconstructed tree:")
print_inorder(root)


def build_bst_from_preorder(preorder):
    def build_bst_from_preorder_util(lower=float('-inf'), upper=float('inf')):
        nonlocal index
        if index == len(preorder):
            return None

        value = preorder[index]
        if value < lower or value > upper:
            return None

        index += 1
        root = BinaryTreeNode(value)
        root.left = build_bst_from_preorder_util(lower, value)
        root.right = build_bst_from_preorder_util(value, upper)
        return root

    index = 0
    return build_bst_from_preorder_util()

# Example usage
preorder = [4, 2, 1, 3, 6, 5, 7]

root = build_bst_from_preorder(preorder.copy())

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

print("Inorder traversal of reconstructed BST:")
inorder_traversal(root)
print("\nPreorder traversal of reconstructed BST:")
preorder_traversal(root)

# Example usage
preorder = [4, 2, 1, 3, 6, 5, 7]

root = build_bst_from_preorder(preorder.copy())

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

print("Inorder traversal of reconstructed BST:")
inorder_traversal(root)
print("\nPreorder traversal of reconstructed BST:")
preorder_traversal(root)


def build_tree_from_inorder_preorder(inorder, preorder):
    if not inorder or not preorder:
        return None

    root_value = preorder.pop(0)
    root = BinaryTreeNode(root_value)

    inorder_index = inorder.index(root_value)

    root.left = build_tree_from_inorder_preorder(inorder[:inorder_index], preorder)
    root.right = build_tree_from_inorder_preorder(inorder[inorder_index + 1:], preorder)

    return root

# Example usage
inorder = [1, 2, 3, 4, 5, 6, 7]
preorder = [4, 2, 1, 3, 6, 5, 7]

root = build_tree_from_inorder_preorder(inorder, preorder.copy())

# A recursive generator that generates Tree leaves in in-order.
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x

        yield t.label

        for x in inorder(t.right):
            yield x

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

print("Inorder traversal of reconstructed tree:")
inorder_traversal(root)
print("\nPreorder traversal of reconstructed tree:")
preorder_traversal(root)
