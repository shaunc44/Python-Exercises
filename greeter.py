from time import sleep
import os

# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.


#### FUNCTIONS ####

def display_title_bar():
	# Clear the screen before listing names
	os.system('clear')

	print("\t**********************************************")
	print("\t***  Greeter - Hello old and new friends!  ***")
	print("\t**********************************************")


#### MAIN PROGRAM ####

# Set up a loop where users can choose what they'd like to do.
choice = ''
while choice != 'q':
	display_title_bar()

	# Let users know what they can do.
	print("\n[1] See a list of friends.")
	print("[2] Tell me about someone new.")
	print("[q] Quit.\n")

	choice = input("What would you like to do? ")

	# Respond to the user's choice.
	if choice == '1':
		print("\nHere are the people I know.\n")
	elif choice == '2':
		print("\nI can't wait to meet this person!\n")
	elif choice == 'q':
		print("\nThanks for playing. Bye.")
	else:
		print("\nI didn't understand that choice.\n")
