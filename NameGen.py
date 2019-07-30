#imports the ability to get a random number (we will learn more about this later!)
from random import *
print("Japanese Name Generator")
#Create the list of words you want to choose from.
First = ["Daichi", "Chitose", "Misaki", "Kisho", "Nari", "Ren", "Tomoe", "Yori"]
Middle = ["Emiko", "Ayako", "Haru", "Ito", "Ozuru", "Usui", "Sorano", "Yumiko"]
#Generates a random integer.
aRandomIndex = randint(0, len(First)-1)
aRandomIndix = randint(0, len(Middle)-1)
print(First[aRandomIndex])
print(Middle[aRandomIndix])
