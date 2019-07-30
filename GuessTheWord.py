import random

# A list of words that
words = ["animal", "room", "sunflower", "job", "sneakers"]
iter = 0
word = random.choice(words)
blank = []
for let in word:
	blank.append("_")
print("The word is: ",blank, ", make a guess!")
# Use to test your code:
word = word.lower()
guesses = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
maxfails = len(word) + 5
fails = 0
fails = fails+1
win = 0
while fails == maxfails:
	break
while fails < maxfails:
	print (blank)
	guess = input("Guess a letter: ")
	if win == len(word):
		print("You win!")
	if len(guess) != 1:
		print ("Only guess one letter at a time!")
	elif guess not in ('abcdefghijklmnopqrstuvwxyz'):
		print ("Please only guess letters!")
		print("You have " + str(maxfails - fails) + " tries left!")
	# check if the guess is valid: Is it one letter? Have they already guessed it?
	for let in word:
		if guess in word:
			blank.pop(word.find(guess))
			blank.insert(word.find(guess), guess)
			win+=1
			print("Correct! You have " + str(maxfails - fails) + " tries left!")
			break
		if let not in word:
			print("Whoops! Try again.", "You have " + str(maxfails - fails) + " tries left!")
			break
		if guess == word:
			print("You got it!")
			break
		fails = fails+1
	while fails == maxfails:
		print("Oh no! The word was", word, ".")
		break



	# check if the guess is correct: Is it in the word? If so, reveal the letters!
