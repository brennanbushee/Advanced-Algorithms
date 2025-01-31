class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTreePostOrderIterator:
    def __init__(self, root: BinaryTreeNode):
        self.stack1 = []
        self.stack2 = []
        if root:
            self.stack1.append(root)
            while self.stack1:
                node = self.stack1.pop()
                self.stack2.append(node)
                if node.left:
                    self.stack1.append(node.left)
                if node.right:
                    self.stack1.append(node.right)

    def has_next(self) -> bool:
        return len(self.stack2) > 0

    def next(self) -> int:
        if not self.has_next():
            return 0
        return self.stack2.pop().value


class BinaryTreeLevelOrderIterator:
    def __init__(self, root: BinaryTreeNode):
        self.queue = []
        if root:
            self.queue.append(root)

    def has_next(self) -> bool:
        return len(self.queue) > 0

    def next(self) -> int:
        if not self.has_next():
            return 0
        current = self.queue.pop(0)
        if current.left:
            self.queue.append(current.left)
        if current.right:
            self.queue.append(current.right)
        return current.value


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

    # Post-order traversal
    post_order_iterator = BinaryTreePostOrderIterator(root)
    print("Post-order traversal:")
    while post_order_iterator.has_next():
        print(post_order_iterator.next(), end=" ")

    print("\n")

    # Level-order traversal
    level_order_iterator = BinaryTreeLevelOrderIterator(root)

    print("Level-order traversal:")
    while level_order_iterator.has_next():
        print(level_order_iterator.next(), end=" ")
