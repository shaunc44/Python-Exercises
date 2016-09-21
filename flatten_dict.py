def flat_dict(dict):

	print 'Regular Dict:', dict

	for i in dict:
		print dict.keys().values() 





dict = {'Name': 'Shaun',
		'Age': 124,
		'Kids': ('Igbert', 'Pumpkin')
		}

print flat_dict(dict)