from time import sleep
import os

# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.

def display_title_bar():
	# Clear the screen before listing names
	os.system('clear')

	print("\t**********************************************")
	print("\t***  Greeter - Hello old and new friends!  ***")
	print("\t**********************************************")


# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']

# Print each name 5 times
for name in names:
	display_title_bar()
	print("\n\n")

	for x in range(0,5):
		print (name.title())

	# Pause for 1 second bw batches
	sleep(1)