class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeLevelOrderIterator:
    def __init__(self, root: BinaryTreeNode):
        self.queue = []
        if root:
            self.queue.append(root)

    def has_next(self) -> bool:
        return len(self.queue) > 0

    def next(self) -> BinaryTreeNode:
        if not self.has_next():
            return None
        current = self.queue.pop(0)
        if current.left:
            self.queue.append(current.left)
        if current.right:
            self.queue.append(current.right)
        return current



def clone_binary_tree(root: BinaryTreeNode) -> BinaryTreeNode:
    if not root:
        return None

    # Dictionary to map original nodes to their clones
    node_map = {}

    # Create the root clone
    new_root = BinaryTreeNode(root.value)
    node_map[root] = new_root

    # Level-order traversal iterator for the original tree
    iterator = BinaryTreeLevelOrderIterator(root)

    # Queue to manage nodes in the cloned tree
    queue = [(root, new_root)]

    while iterator.has_next():
        current = iterator.next()
        if not current:
            continue

        current_clone = node_map[current]

        if current.left:
            left_clone = BinaryTreeNode(current.left.value)
            current_clone.left = left_clone
            node_map[current.left] = left_clone
            queue.append((current.left, left_clone))

        if current.right:
            right_clone = BinaryTreeNode(current.right.value)
            current_clone.right = right_clone
            node_map[current.right] = right_clone
            queue.append((current.right, right_clone))

    return new_root


# Example usage
if __name__ == "__main__":
    # Constructing a sample binary tree
    #        4
    #      /   \
    #     2     5
    #    / \   / \
    #   1   3 6   7
    root = BinaryTreeNode(4)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(5)
    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    # Clone the binary tree
    cloned_root = clone_binary_tree(root)


    # Level-order traversal to print the cloned tree
    def print_level_order(root: BinaryTreeNode):
        if not root:
            return
        queue = [root]
        while queue:
            current = queue.pop(0)
            print(current.value, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


    print("Original tree level-order traversal:")
    print_level_order(root)
    print("\nCloned tree level-order traversal:")
    print_level_order(cloned_root)
