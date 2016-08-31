def fibonacci(num):

	a, b = 0, 1

	i = 0
	while i < num:
		if i < 2:
			print i
			i += 1
		else:
			c = a + b
			print c
			a = b
			b = c
			i += 1

fibonacci(7)