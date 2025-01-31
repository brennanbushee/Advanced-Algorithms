from linked_lists.find_nth_node import LinkedListNode


def split_even_odd(head: LinkedListNode) -> [LinkedListNode, LinkedListNode]:
    even_dummy = LinkedListNode(0)  # Dummy head for the even list
    odd_dummy = LinkedListNode(0)   # Dummy head for the odd list

    even_tail = even_dummy
    odd_tail = odd_dummy

    current = head
    while current:
        if current.value % 2 == 0:
            even_tail.next = current
            even_tail = even_tail.next
        else:
            odd_tail.next = current
            odd_tail = odd_tail.next
        current = current.next

    # Terminate the two lists
    even_tail.next = None
    odd_tail.next = None

    return [even_dummy.next, odd_dummy.next]

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = LinkedListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = LinkedListNode(value)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    print(values)

# Example usage
if __name__ == "__main__":
    N = 3
    original_list = create_linked_list(range(1, N + 1))
    even_head, odd_head = split_even_odd(original_list)

    print("Even List:")
    print_linked_list(even_head)

    print("Odd List:")
    print_linked_list(odd_head)
