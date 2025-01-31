class Queue:
    def __init__(self):
        self.back_end = []  # Stack to handle enqueue operations
        self.front_end = []  # Stack to handle dequeue operations

    def enqueue(self, value: int):
        self.back_end.append(value)

    def dequeue(self) -> int:
        if not self.front_end:
            if not self.back_end:
                return -1  # Queue is empty
            while self.back_end:
                self.front_end.append(self.back_end.pop())
        return self.front_end.pop() if self.front_end else -1

# Example usage
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())  # Output: 1
    print(queue.dequeue())  # Output: 2
    print(queue.dequeue())  # Output: 3
    queue.enqueue(4)
    print(queue.dequeue())  # Output: 4
    print(queue.dequeue())  # Output: -1 (Queue is empty)
