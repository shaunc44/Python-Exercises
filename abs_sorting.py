def abs_sorting(*num_tuple):

	num_list = list(num_tuple)

	for x in range(0, len(num_list)):
		for y in range(0, len(num_list)):
			if abs(num_list[x]) < abs(num_list[y]):
				a = num_list[x]
				num_list[x] = num_list[y]
				num_list[y] = a
	return num_list

print abs_sorting(-4, 3, 2, 1)