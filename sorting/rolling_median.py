import heapq
from collections import defaultdict


class RollingMedian:
    def __init__(self):
        self.low = []  # Max-heap (inverted to min-heap using negative values)
        self.high = []  # Min-heap
        self.delayed = defaultdict(int)  # Delayed deletion counts

    def add(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

        self._balance_heaps()

    def _balance_heaps(self):
        while self.low and self.delayed[-self.low[0]] > 0:
            self.delayed[-self.low[0]] -= 1
            heapq.heappop(self.low)
        while self.high and self.delayed[self.high[0]] > 0:
            self.delayed[self.high[0]] -= 1
            heapq.heappop(self.high)

    def remove(self, num):
        self.delayed[num] += 1
        if num <= -self.low[0]:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        else:
            heapq.heappush(self.low, -heapq.heappop(self.high))
        self._balance_heaps()

    def get_median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (self.high[0] - self.low[0]) // 2  # Floor of the mean


def rolling_median_with_removal(k, initial_stream, append_stream):
    rm = RollingMedian()
    results = []

    # Process initial stream
    for num in initial_stream:
        rm.add(num)
        if len(initial_stream) > k:
            rm.remove(initial_stream[0])
            initial_stream.pop(0)
        results.append(rm.get_median())

    # Process append stream
    for num in append_stream:
        rm.add(num)
        if len(initial_stream) >= k:
            rm.remove(initial_stream[0])
            initial_stream.pop(0)
        initial_stream.append(num)
        results.append(rm.get_median())

    return results


# Example usage:
initial_stream = [1, 2, 3]
append_stream = [4, 5, 6, 7, 8, 9]
results = rolling_median_with_removal(3, initial_stream, append_stream)
print("Rolling medians after each insertion:")
print(results)  # Output should reflect rolling medians after each insertion.
