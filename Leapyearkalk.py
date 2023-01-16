'''
Leap Year calculator.
'''
#Objective of this calculator is to find out if the given year is a leap year or not.
print("Welcome to the Leap Year calculator!")
#Asks to check a year for you.
year = int(input("Which year do you want to check?\n"))
#første if statement som sjekker om årstallet er rent delelig med 4, altså at svaret blir 0(False).
if year % 4 == 0:
    #Andre if statement som sjekker om at tallet er rent delelig med 100, hvis ikke er det skudd år. 
    if year % 100 == 0:
        #Den siste if statementen sjekker om årstallet er rent delelig med 400, hvis det er det så er det faktisk et skudd år.
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")