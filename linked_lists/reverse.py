class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head: LinkedListNode) -> LinkedListNode:
    prev = None
    current = head

    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the current node's pointer
        prev = current  # Move prev and current one step forward
        current = next_node

    return prev  # prev will be the new head

# Helper function to create a linked list from a list
def create_linked_list(lst):
    head = LinkedListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = LinkedListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.value)
        current = current.next
    return lst

# Example usage and test cases
def test_reverse_linked_list():
    head = create_linked_list([1, 2, 3, 4, 5])
    three = create_linked_list([1,2,3])
    singleton = create_linked_list([1])
    # /empty = create_linked_list([])


    # Reverse the linked list: [5, 4, 3, 2, 1]
    new_head = reverse_linked_list(head)
    assert linked_list_to_list(new_head) == [5, 4, 3, 2, 1]
    assert linked_list_to_list(reverse_linked_list(singleton)) == [1]
    assert linked_list_to_list(reverse_linked_list(three)) == [3,2,1]

    print("All test cases pass")

if __name__ == "__main__":
    test_reverse_linked_list()
