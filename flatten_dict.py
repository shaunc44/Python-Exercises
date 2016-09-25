def flat_dict(person):

	for key in person.values():
		for value in key:
			print value

"""
	for key, value in person.items():
		print key, value
"""


"""
	key_list = dict.keys()
	print key_list
	#print dict.get(1)[0]

	for i in range(len(dict.keys())):
	#for i, j in dict.items():
		#for j in range(len(dict.values())):
		#print "\"" + dict.keys()[i] + "\"/\"" + dict.values()[i] + "\""
		#if dict.values()[i]
		#print i
		print dict.get(key_list[1])

#*** use this to print each value
#dict.get('Kids')[0]

	i = 0
	for i in value:
		for key, value[i] in dict.items():
			print "\"" + str(key) + "\"/\"" + str(value) + "\""
"""

person = {'Name': 'Shaun',
		'Age': '97',
		'Kids': ['Scrunchy', 'Pumpkin']
		}

flat_dict(person)