from src.math_lib import square, factorial, is_prime, gcd, lcm

def main():
	print("=== Demostración de librería matemática ===")

	# square
	print(f"square(5) = {square(5)}")
	print(f"square(-3) = {square(-3)}")

	# factorial
	print(f"factorial(5) = {factorial(5)}")
	print(f"factorial(0) = {factorial(0)}")

	# is_prime
	for n in [1, 2, 9, 17]:
		print(f"is_prime({n}) = {is_prime(n)}")

	# gcd
	print(f"gcd(54, 24) = {gcd(54, 24)}")

	# lcm
	print(f"lcm(4, 6) = {lcm(4, 6)}")

if __name__ == "__main__":
	main()