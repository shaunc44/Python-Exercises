#Create function to find min number
def min(*args):
	args = list(args)
	low = args[0]
	for i in args:
		if i < low:
			low = i
	return low


#Create function to find max number
def max(*args):
	args = list(args)
	print args
	high = args[0]
	for i in args:
		if i > high:
			high = i
	return high


print 'Min:', min(-3, 2, 51, 9, 4, 51, 0, -3)
print 'Max:', max([1, 2, 0, 3, 4])