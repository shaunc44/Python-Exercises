# Program that finds the Nth power of the Nth element
# in an array and returns -1 if N is outside the array
# Example - indexWithPower([1, 3, 5, 6], 2) = 25

def indexPower (array, n):
	if (n > len(array)-1):
		return -1
	else:
		return array[n]**n

	indexArray[array, n]

	#return None

print ('This program will take an array and raise the Nth')
print ('element to the Nth power based on index position\n')
print ('Example: ([1, 4, 8, 7], 2) = 64\n\n')

num_array = list()
elements = raw_input ('Enter how many elements you want: ')
print ('\nEnter each number in the array: ')

for i in range(int(elements)):
	n = raw_input('num: ')
	num_array.append(int(n))
print 'Array:', num_array

print ('\nEnter the index position of the element')
print raw_input('you would like to exponentiate? ')