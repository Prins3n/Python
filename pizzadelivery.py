"""
Welcome to the pizza delivery app!
"""
#Printer en hyggelig hilsen.
print("Welcome to Python Pizza Deliveries!")
#input variabel som spør om hvilken størrelse kunden vil ha.
size = input("What size pizza do you want? S, M or L?\n")
#input variabel som spør om kunden vil ha pepperoni på pizzaen sin.
add_pepperoni = input("Do you want pepperoni? Y or N.\n")
#input variabel som spør om kunden vil ha ekstra ost på pizzaen sin.
extra_cheese = input("Do you want extra cheese on that? Y or N.\n")
#variabel som sier verdien til pizza er 0 i nåværende tidspunkt.
pizza = 0
#variabel som sier verdien til regningen er 0 i nåværende tidspunkt.
bill = 0

#if setning som sier at hvis inputen til size er "S" gjør følgende.
if size == "S":
    #øk verdien av regningen med 15.
    bill += 15
    #nye verdien til pizza er nå strengen "small pizza"
    pizza = "small pizza "
#elif setning som sier at hvis størrelsen kunden har tastet inn er "M" gjør følgende.
elif size == "M":
    #øker verdien til regningen til 20.
    bill += 20
    #setter ny verdi på pizza variabelen til "medium pizza"
    pizza = "medium pizza "
#elif setning som sier at hvis størrelsen kunden har tastet inn er "L" gjør følgende.
elif size == "L":
    #øker verdien til regningen til 25.
    bill += 25
    #Setter ny verdi for pizza variabelen til "large pizza"
    pizza = "large pizza "
#else setning som sier at hvis brukeren har tastet inn noe annet 
else:
    print("Invalid input. Valid inputs are the following: 'S', 'M' and 'L'")
#hvis add_pepperoni variabelen er lik "Y", gjør følgende:
if add_pepperoni == "Y":
    #if setning som sier at hvis størrelsen kunden har tastet inn er lik "S" gjør følgende:
    if size == "S":
        #økverdien av bill med ytterligere 2.
        bill += 2
    #hvis størrelsen ikke er "S", da må den være "M" eller "L" og prisen for pepperoni på de pizzastørrelsene var "3".
    else:
        #så da vill regningen bli økt med ytterligere 3.
        bill += 3
    #pizza variabelen øker med strengen under.
    pizza += "with pepperoni "
#hvis svaret var "N", øker pizza variabelen med "without pepperoni".
else:
    pizza += "without pepperoni "
#Hvis kunden har tastet inn "Y" på spørsmålet om de vil ha ekstra ost gjør følgende.
if extra_cheese == "Y":
    #øk regningen med ytterlige 1
    bill += 1
    #øk veriden til pizza med strengen "and with extra cheese"
    pizza += "and with extra cheese"
#hvis kunden ikke ville ha extra ost så økes verdien med tekststrengen "and without extra cheese."
else:
    pizza += "and without extra cheese"

#print setning som innebærer enn f streng, med variablene pizza og bill.
print(f"You have ordered a {pizza}, it will be {bill}$, hope its good.")