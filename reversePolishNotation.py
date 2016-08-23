def rpn(equation):
	eq_list = equation.split()

	while len(eq_list) >= 3:
		if len(eq_list) <= 3:
			return eval(eq_list)
		else:
			list.insert(1, list[2])
			result = eval(list[0:3])
			list.remove(list[0:3])
			list.insert(0, result)


equation = "3 4 +"
#print (rpn(equation))
print rpn(equation)
#eq_parts = equation.split()
#print len(eq_parts)


# 1. parse the string
# 2. arrange first part by .ifnum etc and then calculate first expression
# 3. arrange second part

# How to separte operators?  What data type is an operator in python?

