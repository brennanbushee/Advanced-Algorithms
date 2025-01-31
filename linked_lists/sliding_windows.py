import random
from collections import deque
from typing import List


def sliding_window_max(lst: List[int], w: int) -> List[int]:
    if not lst or w == 0:
        return []

    dq = deque()  # stores indices of useful elements for each window
    max_values = []  # to store the maximum values of each window

    for i in range(len(lst)):
        # Remove elements not part of the window
        if dq and dq[0] < i - w + 1:
            dq.popleft()

        # Remove elements that are less than the current element
        while dq and lst[dq[-1]] < lst[i]:
            dq.pop()

        dq.append(i)

        # Start collecting results when the first window is complete
        if i >= w - 1:
            max_values.append(lst[dq[0]])
        print([(dq[i],lst[dq[i]]) for i in range(len(dq))])
    return max_values


# Example usage
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    w = 3
    #decreasing = [6,0,7]
    random.shuffle(lst)  # Shuffle the list to make it random
    print(f"Shuffled list: {lst}")

    max_values = sliding_window_max(lst, w)
    print("Max values in each window:", max_values)
