import heapq


def kth_largest(k, initial_stream, append_stream):
    # Create a min-heap of size k
    heap = initial_stream[:k]
    heapq.heapify(heap)

    # Add the remaining elements from the initial stream to the heap
    for num in initial_stream[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num)

    # Prepare the answer list
    answer = []

    # Process the append stream
    for num in append_stream:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heappushpop(heap, num)
        # Append the kth largest element to the answer list
        answer.append(heap[0])

    return answer


# Example usage:
k = 3
initial_stream = [4, 5, 8, 2]
append_stream = [3, 5, 10, 9, 4]
print(kth_largest(k, initial_stream, append_stream))  # Output: [4, 5, 5, 8, 8]
