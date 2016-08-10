# FizzBuzz function
def checkNum(num):
	if ((num % 3 == 0) and (num % 5 == 0)):
		return ('FizzBuzz')
	elif (num % 3 == 0):
		return ('Fizz')
	elif (num % 5 == 0):
		return ('Buzz')
	else:
		return str(num)

# User interaction and explanation of game
print ('Hello! This is the FizzBuzz game\n')
print ('If you enter a number divisible by 3 it will return \"Fizz\"\n')
print ('If you enter a number divisible by 5 it will return \"Buzz\"\n')
print ('If you enter a number divisible by 3 and 5 it will return \"FizzBuzz\"\n')
print ('Lastly, if the number entered IS NOT divisible by 3 and/or 5 it will return the number entered\n')
userNum = input('Please enter a number: ')

# Call FizzBuzz function
print('\n' + checkNum(userNum))