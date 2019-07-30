#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
print(type(f))


print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:


for word in f:
    w = word.strip()
    h = test_password.strip()
    p = h.lower()
    a = p.replace("4", "a")
    b = a.replace("0", "o")
    c = b.replace("3", "e")
    d = c.replace("5", "s")
    e = d.replace("1", "l")
    f = e.replace("$", "s")
    g = f.replace("", "")
    if f == w:
        print("Weak password!")

    elif len(p) < 6:
        print("Password is too short!")
        break
