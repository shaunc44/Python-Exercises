def KelvinToFahrenheit(Temperature):
	assert (Temperature >= 0),"Colder than absolute zero!"
	return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
#This one throws the error
print (KelvinToFahrenheit(-5))

###########
#ASSERT STATEMENTS
# 1. assert stmts throw an error message is there an error in your code
# 2. if the assert stmt passes that your repl will display nothing