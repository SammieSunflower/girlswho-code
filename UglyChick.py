
# Update this text to match your story.
start = '''
You are a rare brown chick. You go outside to play by the chicken coop by yourself. Suddenly, two chicks walk up to you. It’s Donald and Daisy.
Donald says “ Your different! Your feathers look funny.”
Daisy says “You are just an annoying duck. Grow up already!”
You scream “Leave me alone!” and run away.
You come across a path that splits into two. The left one leads to the forest and the right one to the boardwalk.

'''

print(start)
Left = '''
You decide to go left and you walk straight into the forest, unaware of what's hidden. You shudder, afraid of the hidden dangers. You’ve never been here before, when suddenly, you hear the bushes shake. Do you go EXPLORE it or IGNORE it?
'''
print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print(Left) # Update to match your story.
    print("Type 'explore' to explore or 'ignore' to ignore")
    if user_input == "explore":
        print(Explore)
    if user_input == "ignore":
        print()

    # Continue code to finish story.

elif user_input == "right":
    print("You choose to go right and ...") # Update to match your story.

    # Continue code to finish story.
