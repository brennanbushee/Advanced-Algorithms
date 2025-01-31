def merge_intervals(intervals):
    # Sort the intervals based on the starting value
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If the list of merged intervals is empty or if the current interval
        # does not overlap with the previous, simply append it.
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is overlap, so we merge the current and previous intervals.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


from itertools import pairwise


def has_merge_conflict(pull_requests) -> bool:
    pull_requests.sort(key=lambda x: x[0])
    for first, nxt in pairwise(pull_requests):
        if nxt[1] < first[1]:
            return False
    return True

def min_intervals_to_remove(intervals):
#How many intervals need to be removed so that the remaining intervals will all be disjoint?
    if not intervals:
        return 0

    # Sort intervals by start time, and if equal, by end time
    intervals.sort(key=lambda x: (x[0], x[1]))

    # Initialize the end of the previous interval and count of removals
    prev_end = intervals[0][1]
    remove_count = 0

    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if start < prev_end:
            # Overlap found, increment the removal counter
            remove_count += 1
            # Update prev_end to be the minimum of the current end or the previous end
            prev_end = min(prev_end, end)
        else:
            # No overlap, update prev_end to the current end
            prev_end = end

    return remove_count



def can_attend_all_meetings(intervals):
    from itertools import pairwise
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Check for overlaps between consecutive intervals
    for i1, i2 in pairwise(intervals):
        # If the start time of the current meeting is earlier than the end time of the previous meeting
        if i2[0] < i1[1]:
            return 0

    return 1


if __name__ == '__main__':
    intervals1 = [[1, 3], [5, 7], [2, 4], [6, 8]]
    intervals2 = [[1, 11], [13, 50], [51, 51], [100, 154]]
    print(has_merge_conflict(intervals1),has_merge_conflict([[1, 4], [5, 8], [9, 10]]))


# Example usage:
intervals1 = [[1, 3], [5, 7], [2, 4], [6, 8]]


print(can_attend_all_meetings([[1, 4], [5, 8], [9, 10]]))  # Output: [[1, 4], [5, 8]]
#print(merge_intervals(intervals2))  # Output: [[1, 11], [13, 50], [51, 51], [100, 154]]
