class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def all_paths_of_a_binary_tree(root):
    def dfs(node, current_path, all_paths):
        if not node:
            return

        # Add the current node's value to the path
        current_path.append(node.value)

        # If it's a leaf node, add the current path to all_paths
        if not node.left and not node.right:
            all_paths.append(list(current_path))
        else:
            # Otherwise, continue DFS on the left and right children
            dfs(node.left, current_path, all_paths)
            dfs(node.right, current_path, all_paths)

        # Backtrack: remove the current node's value from the path
        current_path.pop()

    all_paths = []
    dfs(root, [], all_paths)
    return all_paths


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def root_to_leaf_paths_sum_k(root, k):
    def dfs(node, current_path, current_sum, all_paths):
        if not node:
            return

        # Add the current node's value to the path and update the sum
        current_path.append(node.value)
        current_sum += node.value

        # If it's a leaf node, check if the current sum equals k
        if not node.left and not node.right:
            if current_sum == k:
                all_paths.append(list(current_path))
        else:
            # Otherwise, continue DFS on the left and right children
            dfs(node.left, current_path, current_sum, all_paths)
            dfs(node.right, current_path, current_sum, all_paths)

        # Backtrack: remove the current node's value from the path and subtract from the sum
        current_path.pop()
        current_sum -= node.value

    all_paths = []
    dfs(root, [], 0, all_paths)
    return all_paths


# Example usage:
# Constructing a sample binary tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.right = BinaryTreeNode(6)

k = 7
paths = root_to_leaf_paths_sum_k(root, k)
print(paths)  # Output: [[1, 2, 4], [1, 3, 3]]

# Example usage:
# Constructing a sample binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
#        \
#         6

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.left.right.right = BinaryTreeNode(6)

# paths = all_paths_of_a_binary_tree(root)
# print(paths)  # Output: [[1, 2, 4], [1, 2, 5], [1, 3, 6]]

