rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#vi importerer random funksjonen for å senere finne ut hva maskinen "velger".
import random
#Først finner vi ut hva brukeren velger.
your_choice = input("what do you choose? 0 for rock, 1 for paper or 2 for scissors. ")
#gjør om valget til et integer. kanskje unødvendig?
choice1 = int(your_choice)
#hvis valget ditt er 0 så vil if statementen printe figuren til rock, som er en stein.
if choice1 == 0:
    print(rock)
#hvis valget ditt er 1 så vil elif statementen printe figuren til paper, som er papir.
elif choice1 == 1:
    print(paper)
#hvis valget ditt er 2 så vil elif statementen printe figuren til scissors, som er saks.
elif choice1 == 2:
    print(scissors)
#hvis valget var noe annet en 0, 1 eller 2 så vil programme skrive ut wrong input.
else:
    print("Wrong input.")

#så må vi lagen en variabel for maskinen sitt "valg".
computer_choice = random.randint(0,2)

#hvis tallet som ble valgt av maskinen er 0 print ut stein.
if computer_choice == 0:
    print("Computer chose:\n", rock)
#hvis tallet i computer_choice variabelen er 1 print ut papir.
elif computer_choice == 1:
    print("computer chose:\n", paper)
#hvis tallet i computer_choice variabelen er 2 print ut saks.
elif computer_choice == 2:
    print("computer chose:\n", scissors)

#hvis valget til brukeren og valget til maskinen er det samme print ut at det ble uavgjort.
if choice1 == computer_choice:
    print("Draw.")
#hvis valget til brukeren er sten og maskinen sitt er papir, så vil den printe ut at du taper.
elif choice1 == 0 and computer_choice == 1:
    print("You lose")
#hvis valget til brukeren er stein og maskinen sitt er saks, så vil den printe ut at du vinner!
elif choice1 == 0 and computer_choice == 2:
    print("You win!")
#hvis valget til brukeren er papir og maskinen sitt er saks, så vil den printe ut at du taper.
elif choice1 == 1 and computer_choice == 2:
    print("You lose.")
#hvis valget til brukeren er papir og maskinen sitt er stein, så vil den printe ut at du vinner!
elif choice1 == 1 and computer_choice == 0:
    print("You win!")
#hvis valget til brukeren er saks og maskinen sitt er stein, så vil den printe ut at du taper.
elif choice1 == 2 and computer_choice == 0:
    print("You lose.")
#hvis valget til brukeren er sakt og maskinen sitt er papir, så vil den printe ut at du vinner!
elif choice1 == 2 and computer_choice == 1:
    print("You win!")
#hvis noe er gått galt her så forstår jeg ingenting.
else:
    print("whatthehell.")