#imports the ability to get a random number (we will learn more about this later!)
from random import *
guesses = 0
#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)
while guesses < 3:
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer
	if guess == aRandomNumber:
		print("You got it!")
		break
	elif guess > aRandomNumber:
		print ("Try again, that's too high")
	else:
		print ("Try again, that's too low")
	guesses = guesses + 1
	print ("Sorry, the number was " + str(aRandomNumber))
