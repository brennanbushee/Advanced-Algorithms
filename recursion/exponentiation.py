def calculate_power(a, b):
    MOD = 1000000007  # Define the modulus value

    def _calculate_power(a, b):
        if b == 0:
            return 1
        half = _calculate_power(a, b // 2)
        half = (half * half) % MOD
        if b % 2 != 0:
            half = (half * a) % MOD
        return half

    return _calculate_power(a, b)


# Example usage:
a = 2
b = 10
print(calculate_power(a, b))  # Output: 1024
