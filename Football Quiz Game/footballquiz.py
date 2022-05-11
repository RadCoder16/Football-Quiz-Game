print("""
	FOOTBALL QUIZ
	""")

print("He is the old time world cup leading top goalscorer.")

name = "miroslav klose"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != name and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Guess his name: ")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Incorrect!")
	print("You are out of guesses.")
else:
	print("Correct!")

#Next Quiz

print("\nWhich club has won the most champions league tittles.")

name = "real madrid"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != name and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Guess the club: ")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Incorrect!\nYou are out of guesses.")
else:
	print("Correct!")

#Next Quiz

print("\nManchester United have the most premier league tittles\nBut which club are behind them with the most EPL tittles.")

name = "liverpool"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != name and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Enter the club: ")
		guess += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Incorrect!\nYou are out of guesses.")
else:
	print("Correct!")

#Next Quiz

print("\nWho has the most premier league appearances.")

name = "ryan giggs"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != name and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Enter his name: ")
		guess += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Incorrect!\nYou are out of guesses.")
else:
	print("Correct!")
