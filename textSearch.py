# Program that counts words in user-entered text
# Mininum length is 3 characters ****(maybe)

def textSearch (text, words):
	count = 0
	#text = text.lower()
	for i in words:
		if i in text:
			count += 1

	return count
	#return 0

text = raw_input('Hello, please enter text to be analyzed: \n')
words = raw_input('Which words would you like to count? \n')

textSearch (text, words)




#print text

'''
print ('Thank you!\n')
print ('Now, please enter the words you would like to count: \n')
words = input()
'''