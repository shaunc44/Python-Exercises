#Function to compare strings
#Converts all input to lowercase
#Does not return duplicates

def string_compare (string1, string2):
	stack = []
	for letter1 in string1.lower():
		for letter2 in string2.lower():
			if letter1 == letter2:
				stack.append(letter1)
	stack = list(set(stack))
	print stack


string1 = 'Yellow'
string2 = 'Submarine'
string_compare(string1, string2)