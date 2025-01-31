from typing import Generic, Optional, TypeVar, Dict
from dataclasses import dataclass

T = TypeVar('T')
U = TypeVar('U')


@dataclass
class Node(Generic[T]):
    key: T
    value: T
    prev: Optional['Node[T]'] = None
    next: Optional['Node[T]'] = None


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None

    def add_to_head(self, node: Node[T]):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node

    def remove_node(self, node: Node[T]):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def move_to_head(self, node: Node[T]):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self) -> Optional[Node[T]]:
        if not self.tail:
            return None
        tail_node = self.tail
        self.remove_node(tail_node)
        return tail_node


class LRUCache(Generic[T]):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[T, Node[T]] = {}
        self.dll = DoublyLinkedList[T]()

    def get(self, key: T) -> Optional[T]:
        node = self.cache.get(key)
        if not node:
            return None
        self.dll.move_to_head(node)
        return node.value

    def put(self, key: T, value: T):
        node = self.cache.get(key)
        if node:
            node.value = value
            self.dll.move_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                tail = self.dll.remove_tail()
                if tail:
                    del self.cache[tail.key]
            new_node = Node(key, value)
            self.dll.add_to_head(new_node)
            self.cache[key] = new_node


# Test cases
def test_lru_cache():
    lru = LRUCache(3)

    lru.put(1, 1)
    assert lru.get(1) == 1
    lru.put(2, 4)
    assert lru.get(1) == 1
    assert lru.get(2) == 4

    lru.put(3, 9)
    assert lru.get(1) == 1
    assert lru.get(2) == 4
    assert lru.get(3) == 9
    lru.put(4, 16)
    assert lru.get(2) == 4
    assert lru.get(3) == 9
    assert lru.get(4) == 16
    assert lru.get(1) is None
    assert lru.dll.tail.value == 4

    lru.put(4, 5)
    assert lru.get(4) == 5
    assert lru.dll.head.value == 5


    print("All test cases pass")


if __name__ == "__main__":
    test_lru_cache()
