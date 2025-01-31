# int_to_roman.py

def intToRoman(num: int) -> str:
    """
    Convert an integer to a Roman numeral.

    Args:
        num (int): Integer input.

    Returns:
        str: Roman numeral representation.
    """
    # Mapping integer values to Roman numeral symbols
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = []

    # Iterate through each Roman numeral
    for value, symbol in values:
        while num >= value:
            result.append(symbol)
            num -= value

    return ''.join(result)


# Test cases
def test_intToRoman():
    test_cases = {
        3: "III",
        4: "IV",
        9: "IX",
        58: "LVIII",
        1994: "MCMXCIV",
        444: "CDXLIV",
        3999: "MMMCMXCIX"
    }

    for number, expected in test_cases.items():
        result = intToRoman(number)
        assert result == expected, f"Failed for {number}: expected {expected}, got {result}"
    print("All test cases passed!")


# Run the test cases
if __name__ == "__main__":
    test_intToRoman()
