def string_compare (string1, string2):

	stack = []

	list1 = list(string1)
	list2 = list(string2)

	for letter1 in list1:
		for letter2 in list2:
			if letter1 == letter2:
				stack.append(letter1)
				return stack
				break
		#else:
		#	print ('No letters match')

		#return stack
		#print (letter1)


string1 = 'cox'
string2 = 'hopex'
print (string_compare(string1, string2))