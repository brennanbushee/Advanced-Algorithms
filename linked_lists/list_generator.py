class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def traverse_linked_list(head: LinkedListNode):
    index = 0
    current = head
    while current is not None:
        yield (index, current.value)
        current = current.next
        index += 1
def create_linked_list(n):
    if n <= 0:
        return None
    head = LinkedListNode(1)
    current = head
    for i in range(2, n + 1):
        current.next = LinkedListNode(i)
        current = current.next
    return head
# Example usage
if __name__ == "__main__":
    # Creating a linked list 1 -> 2 -> 3 -> 4
    head = create_linked_list(6)
    #create_linked_list(10)
    # Using the generator to traverse the list
    traverse_and_square =(value ** 2  for (index, value) in traverse_linked_list(head) if index >= 2 == 0)

    for value in traverse_and_square:
        print(f"Node: {value}")
