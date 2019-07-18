# --- Define your functions below! ---
def intro():
    hi = '''Well hello! I am ChatBot. How is your day?
    '''
    print(hi)
def say_greeting():
    print("What's up?!")
def say_default():
    print("Very much nice.")
def process_input(answer):
    if answer == ["hi" or "good" or "hola"]:
        say_greeting()
    else:
        say_default()
def game(user_input):
    if user_input == "yes":
        print("OK! How about a riddle.")
        gamey()
    if user_input == "no":
        print("Aww, ok then.")
def gamey():
        riddle = "What's at least 6 inches long, goes in your mouth, and is more fun if it vibrates?"
        print(riddle)
        guess = input()
        answer = "toothbrush"
        if guess == answer:
            print("Good job!")
        else:
            print("It's a toothbrush man. You dirty minded person.")
            print("Let's try another one.")
            gameyy()
def gameyy():
    rid = "I am something people love or hate. I change peoples appearances and thoughts. If a person takes care of them self I will go up even higher. To some people I will fool them. To others I am a mystery. Some people might want to try and hide me but I will show. No matter how hard people try I will Never go down. What am I?"
    print(rid)
    guessy = input()
    ans = "age"
    if guessy == ans:
        print("You brilliant soul!!!")
    else:
        print("Nope! It's age.")

# --- Put your main program below! ---
def main():
    while True:
      intro()
      answer = input("(What will you say?)")
      process_input(answer)
      user_input = input("You want to play a game?(yes or no?)")

      if user_input == "yes":
          game("yes")
      else:
          game("no")
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
