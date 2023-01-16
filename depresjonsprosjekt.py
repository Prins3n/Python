'''
Hvor lenge vi har igjen å leve hvis alle dør når vi blir 90.
'''
alder = int(input("Hvor gammel er du?\n"))

a = 90 - alder
dager = a*365
uker = a*52
måneder = a*12

print(f"Du har {dager} dager igjen, {uker} uker igjen og tilslutt {måneder} måneder igjen.")