def safe_pawns(pawns):

	count = 0
	#print pawns2[0][0]

	for pawn in pawns:
		#place target pawn coordinates in vars: col & num
		#convert col(letter) to ascii value
		col_pawn0 = ord(pawn[0])
		num_pawn0 = int(pawn[1])
		#print type(num_pawn0)
		#print col_pawn0, num_pawn0
		#Determine coords of required support pawns
		col_pawn1 = chr(col_pawn0 - 1)
		#print col_pawn1
		col_pawn2 = chr(col_pawn0 + 1)
		#print col_pawn2
		num_pawn1 = num_pawn2 = str(num_pawn0 - 1)
		#print num_pawn1, num_pawn2
		#num_pawn2 = str(num_pawn0 + 1)
		print col_pawn1 + num_pawn1
		print col_pawn2 + num_pawn2

		#Now concat the 2 support pawns coords and compare to the target pawn..


"""
		if x and ( or ):

		if c2


	pawn1 = .split(c2), c - one letter, 2 - 1, then rejoin
	pawn2 =
"""


# Enter up to 8 pawns (coordinates) from a1 to h8
safe_pawns({'b4', 'd4', 'f4', 'c3', 'e3', 'g5', 'd2'})
# == 6