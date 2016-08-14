# Program that counts a word from a user-entered text

# Function to lowercase text and
# Separate words by space and then count the word
def textSearch (text, word):
	word = word.lower()
	text = text.lower()
	text_joined = ''.join(c 
		if c.isalnum() 
		else ' ' for c in text).split()
	count = text_joined.count(word)
	return str(count)

# User input & interaction
text = raw_input('Please enter some text to be analyzed:\n\n\t')
word = raw_input('\nWhich word would you like to count?\n\n\t')
print ('\nWord Count = ' + (textSearch (text, word)))