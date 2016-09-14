def string_replace(phrase):

	phrase_join = ",".join(phrase)
	phrase_repl = phrase_join.replace("right", "left")

	return phrase_repl


print string_replace("left", "left")