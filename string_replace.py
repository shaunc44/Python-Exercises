def string_replace(*phrase):

	phrase = ",".join(phrase)
	phrase = phrase.replace("right", "left")
	return phrase

print string_replace("right now I would like to do the right thing!")