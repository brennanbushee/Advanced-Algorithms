class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_collect(root):
    if not root:
        return []

    from collections import deque

    result = []
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()

        if len(result) <= level:
            result.append([])

        result[level].append(node.value)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return result

# Example usage
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

print("Level order traversal collected into lists:")
print(level_order_collect(root))
