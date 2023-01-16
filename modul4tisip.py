"""def greier(lengde, bredde, høyde):
    return lengde*bredde*høyde

tilbud1 = greier(10,15,20)
tilbud2 = greier(20, 8, 20)
tilbud3 = greier(10,25,15)


print("1: ", tilbud1)
print("2: ", tilbud2)
print("3: ", tilbud3)"""


def valid_input(number):
  if number < 7 and number > 0:
    return True
  return False


def remove_numbers(text):
  new_string = "".join([i for i in text if not i.isdigit()])
  return new_string


def lower_case_text(text):
  return text.lower()


def calculate_size(length, height, width):
  return length*height*width


"""setning1 = "HvOR192for E2r fu89nkSJon23er S2å kje364kt"
setning2 = "Hv820r M56789ye m9Å en 2345prograMM2345ERe 234for å3 b23li g4od9"
setning3 = "6789Python09876 234er 234det 23kjekk345este pro2344grammer3ingsspråk2345et je23 vet9 9om"

def lower_remove(text):
    remove = remove_numbers(text)
    lower_case = lower_case_text(remove)
    return lower_case

print(lower_remove(setning1))

print(lower_remove(setning2))

print(lower_remove(setning3))"""

#oppgave 3
"""def valid_input(number):
  if number < 7 and number > 0:
    return True
  return False

def check_valid_input():
    tall = int(input("skriv inn et tall her.\n"))
    while valid_input(tall):
        print("Gyldig tall")
        tall = int(input("skriv inn et tall her.\n"))
    print("Ugyldig tall")

check_valid_input()"""
"""import random
antall_kast = int(input("Hvor mange kast?"))

def roll_dices(antall_kast):
    sum = 0
    for tall in range(antall_kast):
        kast = random.randint(1,6)
        sum+= kast

    return sum

sum = roll_dices(antall_kast)
print("Sum: ", sum)"""

"""#=5, B=4, C=3, D=2, E=1, F=
def karakter(tall_karakter):
    if (tall_karakter == 5):
        return "A"
    elif (tall_karakter == 4):
        return "B"
    elif (tall_karakter == 3):
        return "C"
    elif (tall_karakter == 2):
        return "D"
    elif (tall_karakter == 1):
        return "E"
    elif (tall_karakter == 0):
        return "F"
    else:
        print("Ugyldig")

tall = int(input("Skriv inn karakter."))

print(karakter(tall))"""

#tall = int(input("Skriv inn karakter."))

def karakter_2(tall_karakter):
    karakter_dict = {5: "A", 4: "B", 3: "C", 2: "D", 1: "E" , 0: "F"}
    if tall_karakter >= 0 and tall_karakter <= 5:
        return karakter_dict[tall_karakter]
    else:
        return "Ugyldig"

#print(karakter_2(tall))

def student(student_nr):
    if (student_nr == 1):
        return "Ola Nordmann"
    elif (student_nr == 2):
        return "Nora Eplesyltetøy"

student_nr = int(input("Skriv inn et student nr. "))
print(student(student_nr))

#def student_kombinert_karakter(student_nr, tall_karakter):
 #   student_person = student(student_nr)
  #  karakter_person = karakter(tall_karakter)