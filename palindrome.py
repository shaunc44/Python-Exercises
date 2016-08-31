def palindrome(sentence):

	#sentence = sentence.lower()
	sentence = ''.join(i for i in sentence
		if i.isalpha()).lower()



palindrome('racecar')