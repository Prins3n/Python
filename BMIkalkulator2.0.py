"""
BMI-Kalkulator
"""
#Float input variabel som skal ta inn hvor høy en person er i meter.
height = float(input("Hvor høy er du?\n"))
#Integer input variabel som skal ta inn hvor mye en person veier.
weight = int(input("Hvor mye veier du?\n"))
#BMI round variabel som deler vekten på resultatet av høyde gange høyde.
bmi = float(weight/(height*height))
#Print setning med f-streng som forteller hvor mye BMIen til personen er.
print(f"BMIen din er {round(bmi)}")
#If statement som sjekker om bmien er under 18.5.
if bmi < 18.5:
    #hvis bmien er under 18.5 så printer den at du er undervektig.
    print("You are underweight.")
#elif statement som sjekker om vekten er mellom 18.5 og 25.
elif bmi >= 18.5 and bmi < 25:
    #her kan vi egentlig sløyfe den første bmi sjekken og bare skrive bmi < 25, siden hvis den første statementen er true så vil ikke denne bli sett engang.
    print("You have normal weight!")
#samme som over.
elif bmi >= 25 and bmi < 30:
    print("You are overweight!")
#samme som over.
elif bmi >= 30 and bmi < 35:
    print("You are obese...")
#else statement som sier at hvis vekten er over 35 så er du for feit.
else:
    print("You are clinically")


'''
kan også gjøres slik
if bmi < 18.5:
    print(You are underweight.)
elif bmi < 25:
    print("You have normal weight!")
elif bmi < 30:
    print("You are overweight!")
elif bmi < 35:
    print("You are obese...")
else:
    print("You are clinically")



'''