'''
Pris og høyde sjekker på tivoli
'''
#printer en hyggelig hilsen.
print("Welcome to the rollercoaster!")
#inputvariabel som ber om høyden til personen for å sjekke om de kan kjøre denne "rollercoaster"
height = int(input("How high are you in cm?\n"))
#Variabel for voksen pris.
#adult = 12
#Variabel for ungdom.
#teenager = 7
#Variabel for barne pris.
#child = 5
bill = 0


#If statement som sier at hvis personen er eller er høyere enn 120 cm så har den lov til å kjøre banen.
if height >= 120:
    #Hvis konditionen er sann så vil print utsagnet under bli printet.
    print("You can ride the rollercoaster!")
    #Når vi har funnet ut om personen kan kjøre banen, så må vi spør hvor gammel personen er for å vite hvor mye det kommer til å koste, og det gjør vi gjennom en input variabel.
    age = int(input("How old are you?\n"))
    #Nøstet if statement som sjekker kondisjonen om at hvis personen er over 18 år så må de betale voksen pris. DENNE VIL KUN BLI SJEKKET HVIS DEN FØRSTE IF SETNINGEN ER True.
    if age < 12:
        #f-streng som sier hvor mye personen må betale.
        bill += 5
        #print(f"You will have to pay {bill} to ride this rollercoaster.") utgått.
    #else statement som sier at hvis if statementen er false så blir denne kondisjonen aktivert.
    elif age < 18:
        bill += 7
        #print(f"You will have to pay {bill}to ride this rollercoaster.") utgått.
    elif age >= 45 and age <= 55:
        #hvis alderen er mellom 45 og 55 så slipper de å betale for å kjøre.
        bill = 0
    else:
        bill += 12
        #f-streng som forteller hvor mye barnet må betale.
        #print(f"You will have to pay {bill} to ride this rollercoaster") utgått.
    wants_photo = str(input("Do you want a photo? yes or no.\n"))
    if wants_photo == "yes":
        bill += 3
        print(f"Your new price is {bill}.")
    else:
        print("Okay have a nice day.")

#Else statement som sier at hvis personen ikke er over 120 cm så kan desverre denne ikke kjøre banen.
else:
    print("Unfortunately you will need to grow some more to ride this rollercoaster")