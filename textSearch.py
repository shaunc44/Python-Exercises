# Program that counts words in user-entered text
# Mininum length is 3 characters ****(maybe)

def textSearch (text, words):
	count = 0
	text = text.lower()
	for i in words:
		if i in text:
			count += 1

	return str(count)
	#return 0

text = raw_input('Hi, please enter some text to be analyzed:\n\n\t')
words = raw_input('\nWhich words would you like to count?\n\n\t')

print ('\nWord Count = ' + (textSearch (text, words)))