import json

winter = ["january", "february", "september", "october", "november", "december"]
summer = ["march", "april", "may", "june", "july", "august"]

win = 0
summ = 0


question = ["What's your name?", "What's your favorite food?",
 "What month were you born in?", "What is your favorite song?"]
keys = ["name", "food", "month", "song"]
all = []
collect = "yes"
while collect == "yes":
    random_ques = {}
    index = 0
    for s in question:
        ans = input(s)
        random_ques[keys[index]] = ans
        index += 1
    all.append(random_ques)
    collect = input("Would you like to continue collecting data? (yes or no?) ")

    for u in all:
        answ = u["month"]
        if ans in winter:
            win += 1
        if ans in summer:
            summ += 1
        if win > summ:
            print("More people are born in the winter and fall months than the summer and spring months.")
        if summ > win:
            print("More people are born in the summer and spring months than the winter and fall months.")


f = open("new.json", "w")
json.dump(all, f)
f.close()


with open("new.json") as f:
    try:
        old = json.load(f)
    except ValueError:
        old = []
all.extend(old)
f.close()
