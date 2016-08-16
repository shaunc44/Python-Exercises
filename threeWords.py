# This program verifies if three words, with letters
# only, exist in the user-entered text

# This function splits the string input by each space 
# and then counts the words that contain letters only
def threeWords (sentence):
	sentSplit = sentence.split()
	count = 0
	for word in sentSplit:
		if word.isalpha():
			count += 1
	if count >=3:
		return str(True)
	else:
		return str(False)

# Introduction of what this program does
print('This program will print True if your sentence has three words or more and False if it does not.\n')

# Request sentence for user-input
sentence = raw_input('Enter a sentence: ')

# Print bool result of threeWords function
print('\n' + threeWords(sentence))