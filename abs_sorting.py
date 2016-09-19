def abs_sorting(*num_tuple):

	num_list = list(num_tuple)
	#num_list = []
	#n = 0

	a, b, x = 0, 1, 0
	while x < len(num_list):
		#for (num + 1) in num_list:
		if abs(num_list[a]) > abs(num_list[b]):
			num_list[a] = num_list[b]
			a += 1
			b += 1
		else:
			a += 1
			b += 1
		x += 1


print abs_sorting(-20, 5, -9, 30)