'''
Tip Kalkulator prosjekt.
'''
#print setning som printer ut en streng.
print("Welcome to the tip calculator!")
#En float input variabel for størrelsen på regningen.
bill = float(input("What was the total bill? $" ))
#En integer input variabel som tar inn størrelsen på tipset person ønsker å gi.
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
#En input variabel som tar inn hvor mange person som skal dele regningen.
people = int(input("How many people to split the bill? "))
#Totale regningen med tips inkludert.
bill_with_tip = tip / 100 * bill + bill
#variabel som runder av til to desimaler i tillegg til at den finner hvor mye hver person skal betale.
per_pers = round(bill_with_tip/people, 2)
#print setning som forteller hvor mye hver person må betale.
print(f"Each person should pay: ${per_pers}")