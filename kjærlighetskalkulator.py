"""
Velkommen til kjærlighets kalkulatoren
"""
#printer en hyggelig velkomst
print("Welcome to the Love Calculator!")
#lager to variabler til navnene kalkulatoren skal bruke
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#kombinerer begge navnene i en tekst streng.
combined_string = name1 + name2
#formaterer "combined_string" til små bokstaver.
lower_case_string = combined_string.lower()

#variabler som sjekker hvor mange ganger bokstaven er i navnet.
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
#variabel som summerer sammen alle verdiene vi har funnet ut er i navnet.
true = t + r + u + e

#variabler som sjekker hvor mange ganger bokstaven er i navnet.
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
#variabel som summerer sammen alle verdiene vi har funnet ut er i navnet.
love = l + o + v + e

#variabel som legger sammen summene som strenger. slik at det blir feks 5 fra første verdien og 4 fra den andre blir 54.
score = str(true) + str(love)
#variabel som gjør score variabelen om til int slik at vi kan bruke if statements etter på.
total = int(score)

#hvis total er mindre enn 10 eller over 90 så printer den ut strenger.
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
#hvis totalen er mellom 40 og 50, så vil den printe ut strengen.
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together")
#hvis ingen av de over er True, print ut strengen.
else:
    print(f"Your score is {total}.")
