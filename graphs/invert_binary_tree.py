class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invert_tree(root):
    if root is None:
        return None

    # Recursively invert the left and right subtrees
    left_inverted = invert_tree(root.left)
    right_inverted = invert_tree(root.right)

    # Swap the left and right children
    root.left = right_inverted
    root.right = left_inverted

    return root


# Helper function to print the tree in order (for verification)
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)


from collections import deque


def invert_tree_iterative(root):
    if root is None:
        return None

    queue = deque([root])
    while queue:
        current = queue.popleft()
        # Swap the left and right children
        current.left, current.right = current.right, current.left

        # Add the children to the queue
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return root


# Example usage (same tree as before):
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.right = BinaryTreeNode(6)


# Example usage:
# Constructing a sample binary tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
print("Original tree (in-order traversal):")
in_order_traversal(root)
print()

# Invert the tree using iterative method
invert_tree_iterative(root)

print("Inverted tree (in-order traversal):")
in_order_traversal(root)
print()

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.right = BinaryTreeNode(6)

print("Original tree (in-order traversal):")
in_order_traversal(root)
print()

# Invert the tree
invert_tree(root)

print("Inverted tree (in-order traversal):")
in_order_traversal(root)
print()
