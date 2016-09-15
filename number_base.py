def number_base(num, base):

	num = list(num)
	num = num.reverse()

	#reverse order of nums 
	for x in num:
		#for x in num: #do I need this for loop
		if num[x].isalpha():
			num[y] = ord(num[x]) - 55
		else:
			num[y] = num[x]

	for z in num:
		total += num[z] * base ** z

	return total

	print number_base("AF", 16)
	#Should equal 175
	#AF = (Abase16 * 16^1) + (Fbase16 * 6^0)
	#(10*16)+(15*1)=160+15=175