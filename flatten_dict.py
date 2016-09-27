def flat_dict(person):

	stack = [((), person)]
	result = {}
	while stack:
		path, current = stack.pop()
		for k, v in current.items():
			if isinstance(v, dict) and v:
				stack.append((path + (k,), v))
			else:
				result["/".join((path + (k,)))] = v or ''
	return result


person = {
			'Name': {
				'First': 'Shaun',
				'Last': 'C'
			},
			'Age': '97',
			'Kids': {
				'Son': 'Scrunchy',
				'Daughter': 'Pumpkin'
			}
		}

print flat_dict(person)

#Should print something like:
#'Name'/'First': 'Shaun'
#'Name'/'Last': 'C'
#'Age'/'97'
#........