print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
first = input('now choose you want to go left or right 😈')
if first == 'right':
    print('hahaha you fall into a hole Game Over 😈')
else:
    print("good choice you survived😍 but now we are not done here yet 🙂‍↕️")
    second = input("now choose you want to swim the lack to go to the island or jus wait for boat 😈")
    if second == 'swim':
        print("hahaha 😈 no you attacked by my trout GameOver 😏") 
    else:
        print("you survived okay this is a good luck only 😦 but there is one final thing 😈")
        final =input('you have three doors on is red 🔴 one is yellow 🟡 and one is blue 🔵 choose which one you will enter hero 😈')
        if (final == 'red'):
            print("hehehe you enter room full of fire 🔥 game over 😈")
        elif (final == 'blue'):
            print("hehehe you eaten by beasts 🧌 game over 😈")
        else :
            print("you  win and kill me 🎉 ")
