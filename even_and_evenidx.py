# Give a list of N number, create a list comprehension that contains values
# that are even AND even indexed

def find_even_and_even_idx(l):
# for loop
	# new_list = []
	# for idx in range(len(l)):
	# 	if idx % 2 == 0:
	# 		if l[idx] % 2 == 0:
	# 			new_list.append(l[idx])
	# return new_list

# list comprehension
	lst = [ num for num in l[::2] if num % 2 == 0 ]
	return lst



l = [2, 5, 6, 3, 1, 7, 12, 13, 18, 4, 9, 30, 32, 15, 11, 14, 20]
print (find_even_and_even_idx(l))