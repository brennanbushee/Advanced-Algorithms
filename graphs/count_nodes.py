class TreeNode:
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

def count_nodes(root):
    if root is None:
        return 0
    # Count the nodes in the left subtree, right subtree, and the current node
    return 1 + count_nodes(root.left_ptr) + count_nodes(root.right_ptr)

# Example usage:
root = TreeNode(1)
root.left_ptr = TreeNode(2)
root.right_ptr = TreeNode(3)
root.left_ptr.left_ptr = TreeNode(4)
root.left_ptr.right_ptr = TreeNode(5)

node_count = count_nodes(root)
print(f"Number of nodes in the tree: {node_count}")  # Output should be 5
