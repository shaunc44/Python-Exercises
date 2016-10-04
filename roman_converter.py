#Create list of pairs with zip method
#Create tuple of the list
numerals_map = tuple(zip(
	(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
	('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
))


#Convert integers to roman numerals
def roman_converter (num):

	result []


	if num in numerals_map:
		print numerals_map(num[1])




roman_converter(4)