def safe_pawns(pawns):

	print pawns
	count = 0
	pawns = pawns.items()
	print pawns

	for pawn in pawns:
		print pawn(0)
		location = list(pawn)
		print list(location)
		letter = location[0]
		num = location[1]
		letter_dec = ord(letter)
		pawn1 = chr(letter_dec + 1)
		pawn2 = chr(letter_dec - 1)
		pawn1 = letter1 + str(num - 1)
		pawn2 = letter2 + str(num + 1)
		new_num = 2 - 1


"""
		if x and ( or ):

		if c2


	pawn1 = .split(c2), c - one letter, 2 - 1, then rejoin
	pawn2 =
"""


# Enter up to 8 pawns (coordinates) from a1 to h8
safe_pawns({'b4', 'd4', 'f4', 'c3', 'e3', 'g5', 'd2'})
# == 6