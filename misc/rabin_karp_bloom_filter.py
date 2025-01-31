from collections import defaultdict
from pybloom_live import BloomFilter


def print_before_return(func):
    def wrapper(s):
        result = func(s)
        print(f"String: {s}, Longest repeated substring: '{result}'")
        return result

    return wrapper


@print_before_return
def longest_repeated_substring(s: str) -> str:
    def search(length):
        bloom_filter = BloomFilter(capacity=100000, error_rate=0.001)
        substrings = defaultdict(list)
        hash_value = 0
        base = 256
        prime = 10 ** 9 + 7
        base_l = pow(base, length, prime)

        for i in range(length):
            hash_value = (hash_value * base + ord(s[i])) % prime

        bloom_filter.add(hash_value)
        substrings[hash_value].append(0)

        for i in range(1, len(s) - length + 1):
            hash_value = (hash_value * base - ord(s[i - 1]) * base_l + ord(s[i + length - 1])) % prime

            if hash_value in bloom_filter:
                for start in substrings[hash_value]:
                    if s[start:start + length] == s[i:i + length]:
                        return s[start:start + length]
                substrings[hash_value].append(i)
            else:
                bloom_filter.add(hash_value)
                substrings[hash_value].append(i)
        return None

    low, high = 1, len(s)
    result = ""

    while low <= high:
        mid = (low + high) // 2
        found = search(mid)
        if found:
            result = found
            low = mid + 1
        else:
            high = mid - 1

    return result


# Test cases
print(longest_repeated_substring("efabcdhefhabcdiefi"))  # Should print the string and result, then return "abcd"
print(longest_repeated_substring("banana"))  # Should print the string and result, then return "ana"
print(longest_repeated_substring("eieieo"))  # Should print the string and result, then return "ana"
print(longest_repeated_substring("abcdefg"))  # Should print the string and result, then return ""
print(longest_repeated_substring("aaaaa"))  # Should print the string and result, then return "aaaa"
print(longest_repeated_substring("abcabcabc"))  # Should print the string and result, then return "abcabc"
print(longest_repeated_substring("a" * 20000))  # Stress test: should return "a" * 19999
