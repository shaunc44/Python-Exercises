#Create list of pairs with zip method
#Create tuple of the pairs list

numerals_map = tuple(zip(
	(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
	('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
))

#Convert integers to roman numerals
def roman_converter(i):

	result = []
	for integer, numeral in numerals_map:
		#divide input number by interated numeral values from numerals_map to determine total of each numeral needed
		count = int(i/integer)
		#append numeral total from each iteration to report []
		result.append(numeral * count)
		#iterate by reducing input number by value of numerals previously appended
		i -= integer * count
	#Join the appended numerals together
	return ''.join(result)

print roman_converter(1984)
#Should equal MCMLXXXIV