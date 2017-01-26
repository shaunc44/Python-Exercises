def sum_to_n (n):

	if n == 1:
		return 1
	else:
		#return n + n-1 + (n-1)-1 + ((n-1)-1)-1 + ...
		#after 22 is passed into the function, and then sum_to_n runs insides sum_to_n which runs inside sum_to_n ...
		return n + sum_to_n(n-1)


print ( sum_to_n (22) )