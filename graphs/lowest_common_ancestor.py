class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def find_lca(root, a, b):
        # If the root is None, return None
        if root is None:
            return None

        # If either a or b matches the root, return root
        if root == a or root == b:
            return root

        # Look for a and b in the left and right subtrees
        left_lca = find_lca(root.left, a, b)
        right_lca = find_lca(root.right, a, b)

        # If both of the above calls return Non-None, this node is the LCA
        if left_lca and right_lca:
            return root

        # Otherwise, check if the LCA is in the left subtree or the right subtree
        return left_lca if left_lca is not None else right_lca

# Example usage:
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)

a = tree.left.left  # Node 4
b = tree.left.right  # Node 5
lca_node = find_lca(tree, a, b)
print(f"LCA of {a.value} and {b.value} is {lca_node.value}")
