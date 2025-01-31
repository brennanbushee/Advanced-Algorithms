from collections import deque


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next_right = None


def populate_sibling_pointers(root):
    if not root:
        return None

    # Initialize a queue for level-order traversal
    queue = deque([root])

    # Process each level
    while queue:
        # Number of nodes at the current level
        level_size = len(queue)

        # Previous node in the level
        prev_node = None

        # Process all nodes in the current level
        for i in range(level_size):
            node = queue.popleft()

            # Set the next_right of the previous node
            if prev_node:
                prev_node.next_right = node

            # Update the previous node to be the current one
            prev_node = node

            # Enqueue children of the current node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # The last node in the level should point to None
        prev_node.next_right = None

    return root

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

        result[level].append((node.value, node.next_right.value if node.next_right is not None else None))

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return result



# Example usage:
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.right = BinaryTreeNode(6)

populated_root = populate_sibling_pointers(root)
print(level_order_collect(root))
