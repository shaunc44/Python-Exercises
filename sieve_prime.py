def sieve_prime(number):

	sieve_list = []

	for i in range(2, number):
		for z in range(2, i):
			if i % z == 0:
				break
		else:
			#return i
			sieve_list.append(i)

	return sieve_list


print(sieve_prime(15))