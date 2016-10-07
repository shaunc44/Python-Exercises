import random

def rand_100(num1, num2):
	for i in range(num1, num2+1):
		print (random.randint(num1, num2))

rand_100(1, 100)