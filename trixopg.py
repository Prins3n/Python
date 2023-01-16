# coding=utf-8
"""
trix oppgaver
"""

#oppgave 3 #VIKTIG cmd shitft 7 kommenterer ut blokker.

#Sriv ditt navn, tlf og adresse til terminal på samme linje.
#Skriv ditt navn, tlf og adresse til terminal på hver sin linje.

# print("anders, 45265538, vipeveien 30")
# print("anders")
# print("45265538")
# print("vipeveien 30")


"""
Oppgave 4
) Skriv et program som skriver "Hei Verden!" til terminalen.
b) Utvid programmet med en heltallsvariabel alder som har verdien 4.
c) Skriv ut "Alder: " og verdien av alder til terminalen.
d) Legg inn følgende kommentar i programmet: "Nå endrer vi verdien av variabelen alder :".
e) Endre verdien i variabelen alder til din egen alder. Skriv ut en ny linje til terminalen med en passende tekst og den nye verdien til alder.
f) Kjør programmet ditt.
"""

# print("Hei Verden!")
# alder = 4
# print("alder:", alder)
# #nå endrer vi verdien i alder til min alder.
# alder = 27
# print("alder:", alder)

"""
Oppgave 5
Lag et Python-program som skriver 
ut tre linjer med stjerner "*" 
slik at det ser ut som en pyramide på skjermen.
Kjør programmet og gjør endringer inntil du ser
at programmet fungerer slik det skal.
"""

# print("   x  ")
# print("  xxx ")
# print(" xxxxx ")

"""
Oppgave 6
Lag to heltallsvariabler og kall dem a og b. 
Lagre verdiene 4 og 5 i variablene. 
Skriv ut summen av tallene.
"""

# a = 4
# b = 5

# print(a+b)

"""
Oppgave 7
Lag to variabler, en for bredde og en for høyde. 
Bestem selv verdiene. 
Skriv ut verdiene til terminalen. 
Lag en tredje variabel for arealet til rektangelet 
med verdi bredde ganger høyde. Skriv ut arealet til terminalen.
"""

# bredde = 10
# høyde = 5

# print(bredde)
# print(høyde)
# print("areal=", bredde*høyde)

"""
Oppgave 9
Lag et program som inneholder to heltallsvariable, a og b.
Gi variablene verdier som du selv velger. 
Sjekk om a er større enn b, 
og skriv ut til skjerm enten 
"a er større enn b" eller "a er ikke større enn b". 
Varier verdiene du setter for a og b, 
og sjekk at resultatet blir som forventet i alle tilfellene.
"""

# a = 10
# b = 5

# if a > b:
#     print("a er større enn b")
# else:
#     print("b er større enn a")

# a = 10
# b = 15

# if a > b:
#     print("a er større enn b")
# else:
#     print("b er større enn a")

"""
Oppgave 9
"""

# melding = input("skriv inn noe her: ")
# print(melding)

#Oppgave 10
# fav_farge = input("Skriv inn favoritt fargen din her: ")
# farge = fav_farge.lower()

# if farge == "gul":
#     print("Banan!")
# elif farge == "oransj":
#     print("Mandarin!")
# elif farge == "grønn":
#     print("Surt Epple!")
# else:
#     print("drue???")

#Oppgave 10
"""
Skriv et program hvor du definerer to flyttallsvariabler: 
lengde og bredde. Gi disse variabelen verdiene 10.101 og 3.843.
Skriv ut følgende setning ved å bruke 
formatering av utskrift og de to variablene:
"""
# lengde = 10.101
# bredde = 3.843

# print(f"Rektangelet er {float(lengde)} cm langt og {float(bredde)} cm bredt.")

"""
Oppgave 11
"""

svar = "rabat"

sporsmaal = input("hva er hovedstaden i marokko?")
rettsvar = sporsmaal.lower()

if rettsvar == svar:
    print("Helt rett!")
else:
    print("beklager, svaret var", svar)

