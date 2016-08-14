# Program that counts a word from a user-entered text
# Mininum length is 3 characters ****(maybe)

def textSearch (text, words):

	text = text.lower()
	words = words.lower()

	text_joined = ''.join(c 
		if c.isalnum() 
		else ' ' for c in text).split()

	count = 0
	for i in words:
		if i in text_joined:
			count += 1

	return str(count)
	#return 0

text = raw_input('Please enter some text to be analyzed:\n\n\t')
words = raw_input('\nWhich word would you like to count?\n\n\t')

print ('\nWord Count = ' + (textSearch (text, words)))