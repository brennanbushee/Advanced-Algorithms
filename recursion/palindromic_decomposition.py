


def generate_palindromic_decompositions(s):
    def is_palindrome(s):
        return s == s[::-1]

    def decompose(start, path):
        if start == len(s):
            yield '|'.join(path)
            return

        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                print(f"Calling recursively for {s[start:end]}, {path=}")
                yield from decompose(end, path + [s[start:end]])

    return list(decompose(0, []))


# Example usage:
s1 = "abracadabra"
s2 = "racecarhannah"
s3 = "hannah"
print(generate_palindromic_decompositions(s2))
# Using the generator to get one result at a time
# for decomposition in palindromic_decompositions(s3):
#     print(decomposition)
# print(list(palindromic_decompositions(s3)))
# # Collecting results into a list if needed
# decompositions_list = list(palindromic_decompositions(s2))
# print(decompositions_list)
