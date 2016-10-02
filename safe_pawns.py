def safe_pawns(pawns):

	count = 0

	for pawn in pawns:
		#place target pawn y, x coordinates in vars: col & num
		#convert col(letter) to ascii value
		col_pawn0 = ord(pawn[0])
		#convert num coord to int
		num_pawn0 = int(pawn[1])
		#Determine coords of required support pawns
		pawn1 = chr(col_pawn0 - 1) + str(num_pawn0 - 1)
		pawn2 = chr(col_pawn0 + 1) + str(num_pawn0 - 1)

		#Determine if pawn is safe by comparing to need support pawns
		for i in pawns:
			if (i == pawn1 or i == pawn2):
				count += 1
				break

	print count


# Enter up to 8 pawns (coordinates) from a1 to h8
safe_pawns({'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'e5'})
# == 6