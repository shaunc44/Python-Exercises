def largest_prime (num):

	#Create list of divisible numbers
	divisible_nums = []
	for i in range(2, num + 1):
		if num % i == 0:
			divisible_nums.append(i)
	print divisible_nums

	#Determine which divisible number is largest prime
	for x in divisible_nums[::-1]:
		for y in range(2, x):
			if x % y == 0:
				break
		else:
			return x, 'is the largest prime factor'

#Call and print function
print (largest_prime(94))