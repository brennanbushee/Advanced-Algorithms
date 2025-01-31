def is_valid_expression(s: str) -> bool:
    def is_balanced(s: str) -> bool:
        stack = []
        matching_bracket = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack or stack[-1] != matching_bracket[char]:
                    return False
                stack.pop()
        return not stack

    # def is_valid_sequence(s: str) -> bool:
    #     prev_char = ''
    #     for char in s:
    #         if char.isdigit():
    #             if prev_char.isdigit():
    #                 continue
    #             prev_char = char
    #         elif char in '+-*':
    #             if prev_char in '+-*' or prev_char == '':
    #                 return False
    #             prev_char = char
    #         elif char in '([{':
    #             prev_char = ''
    #         elif char in ')]}':
    #             if prev_char in '+-*':
    #                 return False
    #             prev_char = char
    #         else:
    #             prev_char = ''
    #
    #     return prev_char.isdigit() or prev_char in ')]}'

    def is_valid_sequence(expression:str):
        # Filter out brackets
        filtered_s = ''.join(char for char in expression if char not in '()[]{}')

        # Check for valid operators
        for i in range(1, len(filtered_s) - 1):
            if filtered_s[i] in '+-*':
                if not (filtered_s[i - 1].isdigit() and filtered_s[i + 1].isdigit()):
                    return False

        return True


    # Remove all brackets for sequence validation
    filtered_s = ''.join(char for char in s if char not in '()[]{}')
    # Check if the brackets are balanced
    if not is_balanced(s):
        return False
    # Check if the sequence of operators and operands is valid
    return is_valid_sequence(filtered_s)


# Example usage
test_cases = [
    "{(1+2)*3}+4",  # True
    "((1+2)*3*)",  # False
    "(1+(2*3)-4)",  # True
    "(1+(2*3)-4",  # False
    "1+2)*3",  # False
    "1+2*(3+4)",  # True
    "{[(2+3)*5]-6}/7",  # True
    "{[(2+3)*5]-6}/7*",  # False
    "[(1+2)+3]*{4+5}",  # True
    "[(1+2)+3]*{4+5",  # False
]

for expr in test_cases:
    print(f"{expr}: {is_valid_expression(expr)}")
