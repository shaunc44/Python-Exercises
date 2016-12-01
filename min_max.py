#Create function to find min number
def min(*args, **kwargs, key=None):
	print len(args)
	#args = list(args)
	low = args[0]
	for i in args:
		if i < low:
			low = i
	return low


#Create function to find max number
def max(*args, **kwargs, key=None):
	print len(args)
	#args = list(args)
	#print type(args)
	#args.split()
	#print args[0][3]
	high = args[0][0]
	#print high
	for i in args[0]:
		if i > high:
			high = i
	return high

#print list('hello', 'shaun')


print 'Min:', min(-3, 2, 51, 9, 4, 51, 0, -3)
print 'Max:', max([1, 2, 0, 33, 4], 78)

'''
print max('hello')
print max([9, 10, 77], [2, 4], [7, 2])
print max([2, 3, 0])
print max(2.2, 5.6, 5.9)
'''