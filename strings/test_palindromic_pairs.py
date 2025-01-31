import pytest

from strings import longest_substring_two_chars
from rabin_karp import longest_repeated_substring


def load_test_cases(file_path):
    test_cases = []
    with open(file_path, 'r') as f:
        for line in f:
            input_str, expected_output = line.strip().split('|')
            test_cases.append((input_str, int(expected_output)))
    return test_cases

def load_test_cases_str(file_path):
    test_cases = []
    with open(file_path, 'r') as f:
        for line in f:
            input_str, expected_output = line.strip().split('|')
            test_cases.append((input_str, expected_output))
    return test_cases


# can_form_palindrome_pair  # Adjust the import statement based on your project structure
def test_palindrome_pairs():
    from palindromic_pairs import can_form_palindrome_pair
    assert can_form_palindrome_pair(["abcd", "dcba", "lls", "s", "sssll"]) == ["abcd", "dcba"]
    assert can_form_palindrome_pair(["bat", "tab", "cat"]) == ["bat", "tab"]
    assert can_form_palindrome_pair(["race", "car", "arace"]) == ["race", "ecar"]
    assert can_form_palindrome_pair(["abc", "def", "ghi"]) == ["NOTFOUND", "DNUOFTON"]
    assert can_form_palindrome_pair(["a"]) == ["NOTFOUND", "DNUOFTON"]
    assert can_form_palindrome_pair([]) == ["NOTFOUND", "DNUOFTON"]
    assert can_form_palindrome_pair(["a" * 30, "b" * 30, "c" * 30, "a" * 30[::-1]]) == ["a" * 30, "a" * 30[::-1]]


@pytest.mark.parametrize("input_str,expected_output", load_test_cases_str('longest_repeated_substring_pipe.txt'))
def test_longest_repeated_substring(input_str, expected_output):

    assert longest_repeated_substring(input_str) == expected_output


@pytest.mark.parametrize("input_str,expected_output", load_test_cases('longest_two_char_pipe.txt'))
def test_longest_substring_with_two_distinct_chars(input_str, expected_output):
    assert longest_substring_two_chars(input_str) == expected_output


if __name__ == "__main__":
    pytest.main()
