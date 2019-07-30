def cal_total(list_num):
    lol = 0
    lol = sum(list_num)
    #return sum(list_num)
    return lol

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
total = cal_total(list_num)
print (total)



if is_valid_input(answer):
    say_greeting()
else:
    say_default
def is_valid_input(word):
    valid = ["hi", "hola", "wassup", "sup", "lol"]
    if word in valid:
        return True
    else:
        return False


    answer = answer.lower()
