def largest_prime (num):

	divisible_nums = []
	for i in range(2, num + 1):
		if num % i == 0:
			#Create list of divisible numbers
			divisible_nums.append(i)


	for x in divisible_nums:
		for y in range(2, x):
			if x % y == 0:
				z = y
				return z, 'is the largest prime factor'
			else:
				return x, 'is the largest prime factor'


print (largest_prime(11))

# 1 check for primes <= input
# 2 check if input is divisible by highest prime
# 3 return highest prime if divisible
# 4 return input if not