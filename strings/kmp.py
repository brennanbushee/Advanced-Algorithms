import pytest


def print_before_return(func):
    def wrapper(s):
        result = func(s)
        print(f"String: {s}, Partial match table/Longest prefix-suffix: '{result}'")
        return result

    return wrapper


@print_before_return
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        print(f"Starting loop: {i}, {length}, {pattern[:i+1]}")
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    if (len(pattern) > len(text) or len(text) == 0):
        return []
    # store the length of the longest proper prefix of the substring which is also a suffix for each sub-pattern.
    lps = compute_lps(pattern)
    indices = []
    i = 0
    j = 0
    # Loop invariant: indices contains all known indices up to i, j contains the sliding window of text from [i:j-i+1]
    while i < len(text):
        print(f"Starting loop: {i}, {j}, {text[i-j:i+1]}")
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            indices.append(i - j)

            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices


# Test cases
def test_kmp_search():
    assert kmp_search("Ourbusinessisourbusinessnoneofyourbusiness", "business") == [3, 16, 34]
    assert kmp_search("abcabcabc", "abc") == [0, 3, 6]
    assert kmp_search("abcabcabc", "abcabc") == [0, 3]
    assert kmp_search("banana", "ana") == [1,3]
    assert kmp_search("banana", "na") == [2, 4]
    assert kmp_search("banana", "a") == [1, 3,5]
    assert kmp_search("abcd", "ef") == []
    assert kmp_search("mississippi", "issi") == [1, 4]
    assert kmp_search("sassafras", "as") == [1, 7]
    assert kmp_search("sassafras", "sa") == [0, 3]
    assert kmp_search("", "a") == []
    assert kmp_search("aaaaa", "aa") == [0, 1, 2, 3]
    assert kmp_search("a", "a") == [0]
    assert kmp_search("abababab", "abab") == [0, 2, 4]
    print("All test cases pass")

def test_kmp_search_single():
    kmp_search("sassafrasafras", "sassafras")

if __name__ == "__main__":
    test_kmp_search()
