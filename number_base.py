def number_base(char, base):

	#Divide string into individual chars
	char = list(char)
	#Reverse chars
	char = char[::-1]

	#Create empty list
	#Convert chars > ints; append to list
	num = list()
	for x in char:
		if x.isalpha():
			n = ord(x) - 55
			num.append(int(n))
		else:
			n = int(x)
			num.append(int(n))

	#Check if num > base; then return -1
	for y in num:
		if y > base - 1:
			return -1
		#Convert chars to decimal
		else:
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