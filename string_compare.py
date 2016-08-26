def string_compare (string1, string2):

	stack = []

	for letter1 in string1.split():
		for letter2 in string2.split():
			if letter1 == letter2:
				stack.append(letter1)
			else:



string_compare ('dog', 'orangutan')