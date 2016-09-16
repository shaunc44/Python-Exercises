def number_base(num, base):

	#Divide string into individual chars
	num = list(num)
	#Reverse chars
	num = num[::-1]

	for x in num:
		#for x in num: #do I need this for loop
		if num[x].isalpha():
			num[x] = ord(num[x]) - 55
		else:
			num[x] = num[x]

	total = 0
	for z in num:
		total += num[z] * base ** z

	return total

print number_base('AF', 16)
	#Should equal 175
	#AF = (Abase16 * 16^1) + (Fbase16 * 6^0)
	#(10*16)+(15*1)=160+15=175