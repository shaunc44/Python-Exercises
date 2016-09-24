def flat_dict(dict):

	key_list = dict.keys()
	#print key_list[0]
	#print dict.get(1)[0]

	#for i in range(len(dict.keys())):
	for i in dict:
		#for j in range(len(dict.values())):
		#print "\"" + dict.keys()[i] + "\"/\"" + dict.values()[i] + "\""
		#if dict.values()[i]
		print dict.get('Kids')[0]

#*** use this to print each value
#dict.get('keyName')[0]


"""
	i = 0
	for i in value:
		for key, value[i] in dict.items():
			print "\"" + str(key) + "\"/\"" + str(value) + "\""
"""

"""
	for key in dict.keys():
		print key
		for value in dict.values():
			print value
"""




dict = {'Name': 'Shaun',
		'Age': 99,
		'Kids': ['Scrunchy', 'Pumpkin']
		}

flat_dict(dict)