def flat_dict(dict):

	for key in dict.keys():
		for value in dict.values():
			print key, value
			#print value


"""
	for key, value in dict.items():
		print "\"" + str(key) + "\"/\"" + str(value) + "\""
"""



dict = {'Name': 'Shaun',
		'Age': 99,
		'Kids': ('Scrunchy', 'Pumpkin')
		}

flat_dict(dict)