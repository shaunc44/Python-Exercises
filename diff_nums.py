def diff_nums(*args):

	if not args:
		return 0
	else:
		high = max(args)
		low = min(args)
		diff = high - low
		return diff


num_list = [6, 7, 20, 56]
print (diff_nums(num_list))