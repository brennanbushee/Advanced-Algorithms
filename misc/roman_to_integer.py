# roman_to_int.py

def romanToInt(s: str) -> int:
    """
    Convert a Roman numeral to an integer.

    Args:
        s (str): Roman numeral as a string.

    Returns:
        int: The integer representation of the Roman numeral.
    """
    # Roman numeral mappings
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0

    # Iterate over each character in reverse order
    for char in reversed(s):
        current_value = roman_map[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value

    return total


# Test cases
def test_romanToInt():
    test_cases = {
        "III": 3,
        "IV": 4,
        "IX": 9,
        "LVIII": 58,
        "MCMXCIV": 1994,
        "CM": 900,
        "CDXLIV": 444,
        "MMMCMXCIX": 3999
    }

    for roman, expected in test_cases.items():
        result = romanToInt(roman)
        assert result == expected, f"Failed for {roman}: expected {expected}, got {result}"
    print("All test cases passed!")


# Run the test cases
if __name__ == "__main__":
    test_romanToInt()
