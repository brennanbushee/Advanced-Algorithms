

def reverse_string_recursively(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string_recursively(s[1:]) + s[0]

def test_reverse_string_recursively():
    # Test case 1: Reverse a string with even length
    s1 = "hell"
    assert reverse_string_recursively(s1) == "lleh"

    # Test case 2: Reverse a string with odd length
    s2 = "world"
    assert reverse_string_recursively(s2) == "dlrow"

    # Test case 3: Reverse an empty string
    s3 = ""
    assert reverse_string_recursively(s3) == ""

    # Test case 4: Reverse a string with a single character
    s4 = "a"
    assert reverse_string_recursively(s4) == "a"

    # Test case 5: Reverse a string with special characters
    s5 = "!@#$%^"
    assert reverse_string_recursively(s5) == "^%$#@!"

    # Test case 6: Reverse a string with whitespace characters
    s6 = "  Hello, World!  "
    assert reverse_string_recursively(s6) == "  !dlroW ,olleH  "

if __name__ == '__main__':
    test_reverse_string_recursively()
