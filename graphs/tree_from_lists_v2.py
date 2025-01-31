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
