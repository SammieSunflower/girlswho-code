
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
    print("Type 'explore' to explore or 'ignore' to ignore.")
    user_input = input()
    Explore = '''
    You waddle closer to the bush, trembling with fear. You move the bush aside and see… a wizard!
    He asks, “Who goes there?”
    Should you respond POLITELY or RUDELY?
    '''
    Ignore = '''
    You bolt away from the noise. You run through the forest with sounds from various animals getting louder and abundant, until you reach the end of the forest. You see a field of animals. Do you APPROACH or WANDER back into the forest?
    '''
    if user_input == "explore":
        print(Explore)
        print("Type 'polite' or 'rude' for the way you respond to the wizard.")
        user_input = input()
        Polite = '''You respond, “I’m just a wandering chick. I ran away from my home to escape the bullying chicks. I don’t mean trouble!”
        The wizard sympathizes with you. “Aww, poor chick! Why don’t you stay here with me?”
        You happily live the wizard and become a majestic beautiful duck!
        '''
        Rude = '''You joke around, “Your mom!”
        The wizard is not pleased. “You rude chick! You will pay the consequences for your behavior!”
        The wizard raises his wand and you morph into a frog. You hop away to a nearby pond, regretting your decisions.
        '''
        if user_input == "polite":
            print(Polite)
        if user_input == "rude":
            print(Rude)
    if user_input == "ignore":
        print(Ignore)
        print("Type 'approach' to go by the animals or 'wander' to go back into the forest.")
        Approach = '''The field is sunny and warm, with a large amount of bright green grass.
        “Hey you!” someone calls.
        You turn around and see a pack of brown chicks. You play happily with them.
        '''
        Wander = '''You go back into the forest. Night time falls, and the predators come out.
        “Good luck.” Someone murmurs in the distance.
        '''
        if user_input == "approach":
            print(Approach)
        if user_input == "wander":
            print(Wander)

    # Continue code to finish story.

elif user_input == "right":
    Right = '''You waddle along the boardwalk looking around at your surroundings.
    “Hey! Who are you?”
    You whip around to see two other chicks that look exactly like you.
    You respond “I’m a chick, just like you guys! Who are you?”
    They respond, “We’re beach chicks! We’ve lived here for a while. Would you like a tour?”
    Do you go with THEM or go by YOURSELF?
    '''
    print (Right)
    print("Type them or youself")
    user_input = input()
    if user_input == "them":
        Them = '''You answer, “Sure I’d love to tour around!”
        You all wander and explore the boardwalk of the beach. You finally feel apart of a group of chicks that accept you. You have fun playing and eating.
        One of the chicks asks you, “We had fun! Why don’t you stay with us?”
        Do you STAY or LEAVE?
        '''
        Yourself = '''You don’t exactly trust these chicks. “I think I can go explore myself.”
        You wander around the boardwalk and find that it’s hectic. You discover the seagulls and they taunt and bully you. You find refuge under a bench, waiting for the seagulls to pass by.
        '''
        print(Them)# Update to match your story.
        print("Type stay or leave")
        user_input = input()
        if user_input == "stay":
            Stay = '''“I’d love to stay!” You excitedly exclaim.
            You happy live and grow up with the boardwalk chicks.
            '''
            print(Stay)
        if user_input == "leave":
            Leave = '''You feel uncertain, “I feel like I should go back, I don’t think I can be a boardwalk chick yet.”
            You go back to the path you came from, but you get lost. You end up in the forest. You are in too deep and hear the predators come out.
            '''
    if user_input == "yourself":
        print(Yourself)

    # Continue code to finish story.
