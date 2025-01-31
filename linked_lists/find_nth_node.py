class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head: LinkedListNode) -> LinkedListNode:
    dummy = LinkedListNode(0)
    dummy.next = head
    fast = dummy.next
    slow = dummy
    while fast.next is not None:
        fast.next = slow
        slow  = slow.next





    return fast

def swap_nodes(head: LinkedListNode, k: int) -> LinkedListNode:
    if not head or k <= 0:
        return head

    # Initialize two pointers for the head and tail traversal
    fast = head
    slow = head

    # Move fast pointer n-1 steps ahead
    for _ in range(k - 1):
        if fast.next is None:
            return head  # If n is larger than the length of the list, return the original list
        fast = fast.next

    # Save the nth node from the head
    nth_from_head = fast

    # Move both fast and slow pointers to find the nth node from the tail
    fast = fast.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next

    # Now, slow is at the (n-1)th node from the tail, so slow.next is the nth node from the tail
    nth_from_tail = slow.next

    # If both nodes are found, swap their values
    if nth_from_head and nth_from_tail:
        nth_from_head.value, nth_from_tail.value = nth_from_tail.value, nth_from_head.value

    return head

def test_swap_nth_from_head_and_tail():
    head = create_linked_list([1, 2, 3, 4, 7, 0])
    n = 2
    new_head = swap_nodes(head, n)
    assert linked_list_to_list(new_head) == [1, 7, 3, 4, 2, 0]

    head = create_linked_list([1, 2, 3, 4, 5])
    n = 1
    new_head = swap_nodes(head, n)
    assert linked_list_to_list(new_head) == [5, 2, 3, 4, 1]

    head = create_linked_list([1, 2, 3, 4, 5])
    n = 3
    new_head = swap_nodes(head, n)
    assert linked_list_to_list(new_head) == [1, 2, 3, 4, 5]  # Middle element stays the same

    print("All test cases pass")


def remove_nth_from_end(head: LinkedListNode, n: int) -> LinkedListNode:
    dummy = LinkedListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    # Move fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next
        if fast is None:
            return head  # If n is larger than the length of the list, return the original list

    # Move both pointers until fast reaches the end of the list
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # Slow is now just before the node to be removed
    slow.next = slow.next.next if slow.next is not None else None

    return dummy.next


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


def test_reverse():
    head = create_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(reverse(head)))


# Example usage and test cases
def test_remove_nth_from_end():
    head = create_linked_list([1, 2, 3, 4, 5])

    # Remove 2nd from end: [1, 2, 3, 5]
    new_head = remove_nth_from_end(head, 2)
    assert linked_list_to_list(new_head) == [1, 2, 3, 5]

    # Remove 1st from end: [1, 2, 3]
    new_head = remove_nth_from_end(new_head, 1)
    assert linked_list_to_list(new_head) == [1, 2, 3]

    # Remove 3rd from end (which is also the head): [2, 3]
    new_head = remove_nth_from_end(new_head, 3)
    assert linked_list_to_list(new_head) == [2, 3]

    print("All test cases pass")


if __name__ == "__main__":
    test_remove_nth_from_end()
