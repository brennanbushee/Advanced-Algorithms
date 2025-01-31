from heapq import heappush, heappop
from queue import PriorityQueue

from queue import PriorityQueue


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def __lt__(self, other):
        return self.data < other.data

class LinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def merge_k_sorted_lists(lists):
    dummy = LinkedListNode(0)
    merged_list_tail = dummy

    # Create a min-pq
    pq = PriorityQueue()

    # Add the head of each list to the pq
    for node in lists:
        if node:
            pq.put((node.data, node))

    # While the pq is not empty
    while pq:
        # Get the tuple with the smallest value
        _, smallest_node = pq.get()

        # Add the smallest node to the merged list
        merged_list_tail.next = smallest_node
        merged_list_tail = smallest_node

        # If the smallest node has a next node, add it to the pq
        if smallest_node.next:
            pq.put((smallest_node.next.data, smallest_node.next))

    return dummy.next

def merge_two_lists(list1:LinkedListNode, list2:LinkedListNode):
    heads = [list1, list2]
    dummy = LinkedListNode(0)
    merged_list_tail = dummy
    while len(heads) > 1:
        smallest = min(heads, key=lambda node: node.data)
        heads.remove(smallest)
        if smallest.next:
            heads.append(smallest.next)
        merged_list_tail.next = smallest
        merged_list_tail = smallest
        merged_list_tail.next = None
    merged_list_tail.next = heads.pop()
    return dummy.next

from functools import reduce

def merge_sorted_lists(lists):
    if not lists:
        return None
    return reduce(merge_two_lists, lists)


def merge_k_lists(lists):
    dummy = LinkedListNode(0)
    merged_list_tail = dummy
    while len(lists) > 1:
        smallest = min(lists, key=lambda node: node.data)
        print(f"{smallest.data=}, {smallest.next=}")
        lists.remove(smallest)
        if smallest.next:
            lists.append(smallest.next)
        merged_list_tail.next= smallest
        merged_list_tail = smallest
        merged_list_tail.next = None
    merged_list_tail.next = lists.pop()
    return dummy.next



# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = SinglyLinkedListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = SinglyLinkedListNode(value)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current is not None:
        print(type(current))
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage:
list_heads = [
    create_linked_list([1, 4, 5]),
    None,
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6]),
    None,

]
# q = PriorityQueue()
#
# q.put((4, 'Read'))
# q.put((2, 'Play'))
# q.put((5, 'Write'))
# q.put((1, 'Code'))
# q.put((3, 'Study'))
if __name__ == '__main__':
    list_heads = [
        create_linked_list([1, 4, 5]),
        None,
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6]),
        None,

    ]
    list_heads = list(filter(lambda node: node is not None, list_heads))
    print(list_heads)
    # merged_head = merge_two_lists(list_heads[1], list_heads[2])
    merged_head = merge_sorted_lists(list_heads)
    print_linked_list(merged_head)
