from math import gcd
#Given an integer n, generate all simplified fractions between 0 and 1 (exclusive)
# where the denominator is less than or equal to n.
# A fraction is simplified if the numerator and denominator have no common divisors other than 1.
#Return a sorted list of fractions, where each fraction is represented as [numerator, denominator].
def generate_fractions(n):
  fractions = []
  for numerator in range(1,n):
    for denominator in range(numerator+1, n+1):
      if gcd(numerator, denominator) == 1:
        fractions.append([numerator,denominator])
  return fractions
def test_generate_fractions():
    assert generate_fractions(3) == [[1, 2], [1, 3], [2, 3]], "Test case n=3 failed"
    assert generate_fractions(4) == [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]], "Test case n=4 failed"
    assert generate_fractions(5) == [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 5], [3, 4], [3, 5], [4, 5]], "Test case n=5 failed"
    assert generate_fractions(1) == [], "Test case n=1 failed (no fractions between 0 and 1)"
    assert generate_fractions(2) == [[1, 2]], "Test case n=2 failed"
# Run tests
test_generate_fractions()