def largest_prime (num):

	for i in range(1, num + 1):
		if num % i == 0:
			print i


largest_prime(10)

# 1 check for primes <= input
# 2 check if input is divisible by highest prime
# 3 return highest prime if divisible
# 4 return input if not