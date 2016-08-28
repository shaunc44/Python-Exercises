#Function to compare strings
#Converts all input to lowercase
#Does not return duplicates

def string_compare (string1, string2):
	stack = []
	#Compare letters in 1st string to 2nd string
	for letter1 in string1.lower():
		for letter2 in string2.lower():
			if letter1 == letter2 and letter1 not in stack:
				stack.append(letter1)
	#Remove duplicate letters
	#stack = list(set(stack))
	print (stack)


#Enter string inputs and call function
string1 = 'Shaunn'
string2 = 'Submaarinne'
string_compare(string1, string2)