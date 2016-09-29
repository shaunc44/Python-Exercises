def flat_dict(person):

	#Puts tuple, dictionary in 'stack' list
	stack = [((), person)]
	print '1:', stack

	#Creates empty dictionary
	result = {}
	print '2:', result

	#While stack is true???
	while stack:

		#Unpacks stack's tuple in 'path' and stack's 'dictionary' in current
		path, current = stack.pop()
		print '3:', path
		print '4:', current

		#Iterate through key, value of current which is a dict
		for k, v in current.items():
			print '5:', k
			print '6:', v

			#Checks that v is type dictionary and v exists
			if isinstance(v, dict) and v:
				stack.append((path + (k,), v))
				print '7:', stack
			else:
				#What the heck does this do????
				result["/".join((path + (k,)))] = v or ''
				print '8:', result
	return result


person = {
			'Info': {
				'Name': {
					'First': 'Shaun',
					'Last': 'McArthur',
				},
				'Age': '97'
			},
			'Kids': {
				'Son': 'Scrunchy',
				'Daughter': 'Pumpkin'
			}
		}

flat_dict(person)

#Should print something like:
#{'Age'/'97', 'Name'/'First': 'Shaun' .....