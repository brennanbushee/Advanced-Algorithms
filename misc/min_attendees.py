from collections import Counter

# Ask a sample of n people at a work conference how many people they met there with the same title.
# Given their answers, determine the minimum number of people at that conference.
# Similar to the "rabbits in the forest" problem from combinatorics.
def min_attendees(answers):
    # For example, [0,0,1,2], returns {0:2, 1:1, 2:1}.
    count = Counter(answers)
    total_attendees = 0

    for x, freq in count.items():
        group_size = x + 1  # Minimum number of people per group
        num_groups = (freq + group_size - 1) // group_size  # Ceiling division
        total_attendees += num_groups * group_size

    return total_attendees


# Test Cases
def test_min_attendees():
    assert min_attendees([2, 1, 1]) == 5, "Test case [2, 1, 1] failed"
    assert min_attendees([0, 0, 1]) == 4, "Test case [0, 0, 1] failed"
    assert min_attendees([0, 0, 0]) == 3, "All unique titles"
    assert min_attendees([3, 3, 3, 3]) == 4, "All same title group"
    assert min_attendees([5, 5, 5, 5, 5, 5, 2, 5]) == 15, "Test case for clique of 5 failed"
    assert min_attendees([1, 2, 10, 0]) == 17, "Test case for clique of 10 failed"
    assert min_attendees([0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 15, "Gaussian test case for 15 failed"
    assert min_attendees([5]) == 6, "Single person claiming 5 others"
    assert min_attendees([]) == 0, "Empty input"
    assert min_attendees([1, 1, 1, 1]) == 4, "Multiple groups needed"

    print("All test cases passed!")


# Run tests
test_min_attendees()
