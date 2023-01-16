"""
Welcome to the Treasure Island Game.
"""
#print statement som printer bildet under.
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

#lager en input variabel som starter spillet.
xroad = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right".\n').lower()
#sjekker hvis xroad variabelen er venstre i så fall skjer dette.
if xroad == "left":
    print("That was the correct path! Proceed.")
    lake = input('You\'ve come to a a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    #jekker om den nye inputten er "wait". og hvis den er det så lager den en ny input.
    if lake == "wait":
        print("You're gazing into the horizon contemplating your life decisons. Meanwhile a boat boat pulls up to shore.")
        island = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if island == "red":
            red_door = "It's a room full of fire. Game Over."
            print(red_door)
        elif island == "yellow":
            yellow_door = "You found the treasure! You Win!"
            print(yellow_door)
        elif island == "green":
            green_door = "You enter a room of beasts. Game Over."
            print(green_door)
        else:
            invalid_door = "You chose a door that doesn't exist. Game Over."
    else:
        water = "You get attacked by an angry crocodile. Game Over."
        print(water)
else:
    hole = "You fell into a hole. Game Over."
    print(hole)
