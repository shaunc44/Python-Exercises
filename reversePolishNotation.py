def rpn(equation):
	eq_parts = equation.split()

	if len(eq_parts) >= 3:
		block = ""
		for x in eq_parts:
			count = 0
			if x.isnumeric() == True:
				block.append(x)
			else:
				block.insert(1, x)

			result = eval(block)
	else:
		print eval(new_eq)



equation = "3 4 +"
#print (rpn(equation))
print rpn(equation)
#eq_parts = equation.split()
#print len(eq_parts)


# 1. parse the string
# 2. arrange first part by .ifnum etc and then calculate first expression
# 3. arrange second part

# How to separte operators?  What data type is an operator in python?

