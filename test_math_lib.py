import pytest
from math_lib import square, factorial, is_prime, gcd, lcm

def test_square():
	assert square(2) == 4
	assert square(-3) == 9
	assert square(0) == 0


def test_factorial():
	assert factorial(0) == 1
	assert factorial(5) == 120
	with pytest.raises(ValueError):
		factorial(-1)


def test_is_prime():
	assert is_prime(2) is True
	assert is_prime(17) is True
	assert is_prime(1) is False
	assert is_prime(9) is False


def test_gcd():
	assert gcd(54, 24) == 6
	assert gcd(10, 0) == 10
	assert gcd(0, 0) == 0


def test_lcm():
	assert lcm(4, 6) == 12
	assert lcm(0, 5) == 0
	assert lcm(7, 3) == 21

if __name__ == "__main__":
	import sys
	sys.exit(pytest.main([__file__]))