def longest_balanced_subsequence(s: str) -> int:
    # Stack to keep track of the indices of '('
    stack = []
    max_length = 0
    current_length = 0
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')' and stack:
            # When we find a matching pair, we increase the max_length by 2
            stack.pop()
            current_length += 2
        else:
            current_length = 0
        max_length = max(max_length, current_length)

    return max_length

# Example usage and test cases
def test_longest_balanced_subsequence():
    assert longest_balanced_subsequence("()()()") == 6
    assert longest_balanced_subsequence("(()))(()") == 4
    assert longest_balanced_subsequence("(()())") == 6
    assert longest_balanced_subsequence("((()))") == 6
    assert longest_balanced_subsequence("((()()())") == 8
    assert longest_balanced_subsequence("") == 0
    assert longest_balanced_subsequence("((((((((") == 0
    assert longest_balanced_subsequence("))))))))") == 0
    assert longest_balanced_subsequence("((((())(((()") == 6 # Should return 6
    assert longest_balanced_subsequence("()((()))()((()))") == 16 # Should return 14
    assert longest_balanced_subsequence("((((())(((()") == 6 # Should return 6
    print("All test cases pass")

if __name__ == "__main__":
    test_longest_balanced_subsequence()