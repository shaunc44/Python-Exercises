# Function to evaluated Reverse Polish Notation
def rpn(equation):

	# Create list of equation parts and call it stack
	stack = []

	# For loop iterates through each value of equation
	for val in equation.split():
		# If operator, use to calculate 2 nums in stack
		if val in ['-', '+', '*', '/', '**']:
			op1 = stack.pop()
			op2 = stack.pop()
			if val == '-':
				result = op2 - op1
			if val == '+':
				result = op2 + op1
			if val == '*':
				result = op2 * op1
			if val == '/':
				result = op2 / op1
			if val == '**':
				result = op2 ** op1
			stack.append(result)
		# If num, append to stack
		else:
			stack.append(float(val))

	return stack.pop()

equation = "3 4 ** 8 - 27 +"

print rpn(equation)