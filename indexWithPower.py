# Program that finds the Nth power of the Nth element
# in an array and returns -1 if N is outside the array
# Example - indexWithPower([1, 3, 5, 6], 2) = 25

# Function that processes index position from user input
def indexPower (num_array, position):
	if len(num_array) <= position:
		return -1
	else:
		return num_array[position]**position

# Instructions to the user
print ('This program will take an array and raise the Nth')
print ('element to the Nth power based on index position\n')
print ('Example: ([1, 4, 8, 7], 2) = 64\n\n')

# Set up array using list()
num_array = list()

# Ask user for # of elements in array
elements = input('Enter how many elements you want in array: ')

# Ask user to enter each value in the array
print ('\nEnter each number in the array: ')
for i in range(int(elements)):
	n = raw_input('num: ')
	num_array.append(int(n))

# Display array after numbers entered
print 'Array:', num_array

# Ask for index position to be calculated
print ('\nEnter the index position of the element')
position = input('you would like to exponentiate? ')

# Call the function indexPower
print (indexPower (num_array, position))