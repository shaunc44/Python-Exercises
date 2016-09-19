def abs_sorting(*num_tuple):

	num_list = list(num_tuple)
	a = 0

	for x in num_list:
		for y in num_list:
			if abs(x) > abs(y):
				a = x
				x = y
				y = a
	print num_list
			#else:
			#	continue
			#return num_list

print abs_sorting(-20, 5)