
def rpn(equation):
	eq_list = equation.split()
	# this for loop need to change???
	for i in range(len(eq_list)):
		if len(eq_list) < 3:
			return eval(equation)
		else:
			while len(eq_list) > 3:
			#for i in range(len(eq_list)):
				eq_list.insert(1, eq_list[2])
				eq_join = " ".join(eq_list[0:3])
				result = eval(eq_join)
				for i in range(3):
					eq_list.remove(eq_list[0])
				eq_list.insert(0, result)
				return result


equation = "3 4 + 2 *"

print (rpn(equation))