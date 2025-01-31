class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeIterator:
    def __init__(self, root: BinaryTreeNode):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node: BinaryTreeNode):
        while node:
            self.stack.append(node)
            node = node.left

    def has_next(self) -> bool:
        return len(self.stack) > 0

    def next(self) -> int:
        if not self.has_next():
            return 0

        next_node = self.stack.pop()
        self._push_left(next_node.right)
        return next_node.value

# Example usage
if __name__ == "__main__":
    # Constructing a sample binary tree
    #        4
    #      /   \
    #     2     5
    #    / \   / \
    #   1   3 6   7

    root = BinaryTreeNode(4)
    iterator = BinaryTreeIterator(root)

    print(f"{(int(iterator.has_next()))=}")
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(6)
    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(5)
    root.right.right = BinaryTreeNode(7)

    while iterator.has_next():
        print(iterator.next())
