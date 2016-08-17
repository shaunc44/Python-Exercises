# This program verifies that three words occur consecutively
# in the user-entered text.  Each word must consist of
# only letters.

# Introduction of what this program does to the user
print('This program will print True if your sentence has')
print('three words, or more, and False if it does not.\n')

# Run anonymous function to verify if three words
# occur in succession
three_words = lambda sentence: "wordwordword" in "".join(
	'word' if word.isalpha()
	else 'not_word' for word in sentence.split())

# Request sentence for user-input
sentence = raw_input('Enter a sentence: ')

print(three_words(sentence))













# Old program that didn't factor in 3 consecutive words
"""
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
"""