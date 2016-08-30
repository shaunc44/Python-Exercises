def fibonacci(num):

	i = 0
	k = 1

	while k < num:
		if i > 1:
			result =  i + k
			print result
			i = k
			k = result
		else:
			print i
			i += 1



	"""
	while i < num:
		if i > 1:
			result = (i + (i-1))
			return result
			i += 1
		else:
			print i
			i += 1
	"""

fibonacci(5)