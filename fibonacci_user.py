class Fibonacci:

	def __init__(self):
		self.num1 = 0
		self.num2 = 1

	def calc_next_num(self):
		ans = input("Continue: Y or N? ")
		if ans == "N" or "n":
			action = False
			total = self.num1 + self.num2
			return total
		elif ans == "Y" or "y":
			total = self.num1 + self.num2
			next_num = self.num1 = self.num2
			self.num1 = self.num2
			self.num2 = next_num
			return total


f = Fibonacci()

action = True
while action:
	print ( "Next Fibonacci Sequence = ", f.calc_next_num() )



