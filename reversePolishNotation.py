"""
def rpn(equation):
	eq_parts = equation.split()
	#for i in eq_parts:
	#	if i 
	result = eval(equation)

	#return (int(eq_parts[1]) + int(eq_parts[0]))
	#print int(eq_parts[2])

	print result #, "=>", result, type(result)

equation = "3 4 +"

print (rpn(equation))
"""

# 1. parse the string
# 2. arrange first part by .ifnum etc and then calculate first expression
# 3. arrange second part

# How to separte operators?  What data type is an operator in python?

print type(*)