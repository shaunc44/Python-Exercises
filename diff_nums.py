def diff_nums(args):
#Use of (*args) cause typeError problems
	if not args:
		return 0
	else:
		high = max(args)
		low = min(args)
		diff = high - low
		return diff


num_list = [1, 4, 9, 20, -3]
print (diff_nums(num_list))