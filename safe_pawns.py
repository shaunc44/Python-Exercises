def safe_pawns(pawns):

	count = 0

	for pawn in pawns:
		#place target pawn coordinates in vars: col & num
		#convert col(letter) to ascii value
		pawn0 = pawn
		col_pawn0 = ord(pawn[0])
		num_pawn0 = int(pawn[1])
		#print col_pawn0, num_pawn0
		#Determine coords of required support pawns
		col_pawn1 = chr(col_pawn0 - 1)
		#print col_pawn1
		col_pawn2 = chr(col_pawn0 + 1)
		#print col_pawn2
		num_pawn1 = num_pawn2 = str(num_pawn0 - 1)
		#num_pawn2 = str(num_pawn0 + 1)
		pawn1 = col_pawn1 + num_pawn1
		pawn2 = col_pawn2 + num_pawn2

		#Create better logic statement
		#If pawn1 or pawn 2 matches any pawns from input ...
		if (pawn0 and (pawn1 or pawn2)) == True:
			count += 1
	print count


# Enter up to 8 pawns (coordinates) from a1 to h8
safe_pawns({'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'e5'})
# == 6