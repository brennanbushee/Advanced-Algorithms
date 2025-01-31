from linked_lists.find_nth_node import LinkedListNode
class LinkedList:
    def __init__(self):
        self.head = None


def get_length(head: LinkedListNode) -> int:
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length


def get_intersection_node(headA: LinkedListNode, headB: LinkedListNode) -> LinkedListNode:
    if not headA or not headB:
        return -1

    lenA = get_length(headA)
    lenB = get_length(headB)

    currentA = headA
    currentB = headB

    # Align the start point of both lists
    if lenA > lenB:
        for _ in range(lenA - lenB):
            currentA = currentA.next
    else:
        for _ in range(lenB - lenA):
            currentB = currentB.next

    # Traverse both lists together to find the intersection
    while currentA and currentB:
        if currentA == currentB:
            return currentA
        currentA = currentA.next
        currentB = currentB.next

    return -1


# Example usage
if __name__ == "__main__":
    # Creating intersecting linked lists
    # List A: 1 -> 2 -> 3
    #                       \
    #                        6 -> 7 -> 8 -> 9
    #                       /
    # List B: 4 -> 5

    intersecting_node = LinkedListNode(6)
    intersecting_node.next = LinkedListNode(7)
    intersecting_node.next.next = LinkedListNode(8)
    intersecting_node.next.next.next = LinkedListNode(9)

    listA = LinkedList()
    listA.head = LinkedListNode(1)
    listA.head.next = LinkedListNode(2)
    listA.head.next.next = LinkedListNode(3)
    listA.head.next.next.next = intersecting_node

    listB = LinkedList()
    listB.head = LinkedListNode(4)
    listB.head.next = LinkedListNode(5)
    listB.head.next.next = intersecting_node

    intersection = get_intersection_node(listA.head, listB.head)

    if intersection != -1:
        print("Intersecting at node with value:", intersection.value)
    else:
        print("No intersection.")
