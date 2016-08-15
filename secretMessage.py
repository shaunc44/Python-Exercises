# Program that separates uppercase letters which will
# reveal a secret message


# Function to join all uppercase letters and then return them
def secretMessage (msg):
	msg_decoded = ''.join(letter
		for letter in msg
			if letter.isupper())
	return str(msg_decoded)


# User entered message
msg = raw_input('Enter your message to decoded: \n\n\t')


# Output the decoded message
print('\n\nYour secret message is ' + secretMessage(msg))