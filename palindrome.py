def palindrome(sentence):

	sentence = ''.join(i for i in sentence
		if i.isalpha()).lower()
	rev_sentence = sentence[::-1]

	if sentence == rev_sentence:
		return True
	else:
		return False


print palindrome('Was it a car, or a cat, I saw?')