"""
Velkommen til russisk rulett for å bestemme hvem som skal betale for middag idag!
"""
import random
#En input variabel som lagrer navn som brukeren har tastet inn separert med ett komma.
names_string = input("give me everybodys names, separated by a comme.\n")
#en variabel som legger navnene i en liste separert med ett komma.
names = names_string.split(", ")
#variabel som lagrer lengden på lista.
num_items = len(names)
#en variabel som sier at et tall mellom 0 og lengden på lista minus en.
#hvorfor det er viktig med minus en er fordi lista begynner på 0.
tall = random.randint(0, num_items -1) #hvis vi ikke har -1 kan vi lett få "indes error, list index out of range."

#f streng som finner et navn i fra lista etter hvilket tilfeldig tall "tall"-variablen har funnet.
print(f"Idag vil {names[tall]} betale for middag.")

