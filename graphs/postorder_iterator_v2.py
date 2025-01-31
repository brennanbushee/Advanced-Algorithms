class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class PostOrderIterator:
    def __init__(self, root):
        self.stack = []
        self.visited = set()
        if root:
            self.stack.append(root)

    def has_next(self):
        return bool(self.stack)

    def next(self):
        if not self.has_next():
            return None

        while self.stack:
            node = self.stack[-1]
            if (node.left and node.left not in self.visited):
                self.stack.append(node.left)
            elif (node.right and node.right not in self.visited):
                self.stack.append(node.right)
            else:
                self.visited.add(node)
                self.stack.pop()
                return node.value

# Function to collect postorder traversal into a list
def collect_postorder(root):
    iterator = PostOrderIterator(root)
    result = []

    while iterator.has_next():
        result.append(iterator.next())

    return result

# Example usage
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

postorder_list = collect_postorder(root)
print("Postorder traversal collected into a list:")
print(postorder_list)
