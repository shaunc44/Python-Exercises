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

def get_user_choice():
	# Let users know what they can do.
	print("\n[1] See a list of friends.")
	print("[2] Tell me about someone new.")
	print("[q] Quit.\n")

	return input("What would you like to do? ")

def show_names():
	# Shows names of everyone already in the list
	print("\nHere are the people I know.\n")
	for name in names:
		print(name.title())

def get_new_name():
	# Ask user for new name and stores name
	new_name = input("\nPlease tell me this person's name: ")
	names.append(new_name)
	print("\nI'm so happy to know %s!\n" % new_name.title())


#### MAIN PROGRAM ####

# Set up a loop where users can choose what they'd like to do.
name = []
choice = ''
display_title_bar()

while choice != 'q':

	choice = get_user_choice()

	# Respond to the user's choice.
	display_title_bar()
	if choice == '1':
	elif choice == '2':
	elif choice == 'q':
		print("\nThanks for playing. Bye.")
	else:
		print("\nI didn't understand that choice.\n")



