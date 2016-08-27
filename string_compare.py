def string_compare (string1, string2):

	stack = []

	for letter1 in string1:
		for letter2 in string2:
			if letter1 == letter2:
				stack.append(letter1)
				continue
				#return stack
				#break
		#else:
		#	print ('No letters match')
		#return stack
		print stack


string1 = 'cox'
string2 = 'marox'
print (string_compare(string1, string2))