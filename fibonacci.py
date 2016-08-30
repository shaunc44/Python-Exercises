def fibonacci(num):

	num_list = [0, 1]

	i = 0
	print num_list[0]
	print num_list[1]
	while i < num:
		total = num_list[-1] + num_list[-2]
		print total
		num_list.append(total)
		i += 1

print(fibonacci(15))