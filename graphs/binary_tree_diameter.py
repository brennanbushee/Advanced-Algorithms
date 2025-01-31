class TreeNode():
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr


def binary_tree_diameter(root):
    # Helper function to calculate the height of a subtree and update the diameter
    def height(node):
        nonlocal diameter
        if not node:
            return 0
        # Recursively calculate the height of left and right subtrees
        left_height = height(node.left_ptr)
        right_height = height(node.right_ptr)

        # Update the diameter
        diameter = max(diameter, left_height + right_height)

        # Return the height of the current node
        return max(left_height, right_height) + 1

    diameter = 0
    height(root)
    return diameter


# Example usage:
# Constructing a sample binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5

node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, left_ptr=node4)
node3 = TreeNode(3, left_ptr=node5)
root = TreeNode(1, left_ptr=node2, right_ptr=node3)

print(binary_tree_diameter(node2))  # Output: 3
