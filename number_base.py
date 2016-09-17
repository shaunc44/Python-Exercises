def number_base(char, base):

	#Divide string into individual chars
	char = list(char)
	#Reverse chars
	char = char[::-1]

	#Create empty list to insert converted chars
	num = list()
	for x in char:
		if x.isalpha():
			n = ord(x) - 55
			num.append(int(n))
		else:
			n = int(x)
			num.append(int(n))

	#Need to check whether num exceeds bases, return -1

	#return num

	total = 0
	i = 0
	for z in num:
		total += (z * (base ** i))
		i += 1

	return total


print number_base('AF', 16)
	#Should equal 175
	#AF = (Abase16 * 16^1) + (Fbase16 * 16^0)
	#(10*16)+(15*1)=160+15=175