def rpn(equation):
# Evaluate a reverse polish notation

    stack = []

    for val in equation.split(' '):
        if val in ['-', '+', '*', '/']:
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
            stack.append(result)
        else:
            stack.append(float(val))

    return stack.pop()

equation = "3 4 * 8 - 3 / 9 *"

print rpn(equation)