# Print fibo sequence up to but not including input num

def fibonacci(num):

	a, b = 0, 1
	if a < num:
		print a
	if b < num:
		print b

	for i in range (0, num):
		c = a + b
		if c < num:
			print c
		a = b
		b = c

fibonacci(4200)