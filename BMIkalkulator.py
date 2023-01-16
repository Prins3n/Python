"""
BMI-Kalkulator
"""
#Float input variabel som skal ta inn hvor høy en person er i meter.
height = float(input("Hvor høy er du?\n"))
#Integer input variabel som skal ta inn hvor mye en person veier.
weight = int(input("Hvor mye veier du?\n"))
#BMI round variabel som deler vekten på resultatet av høyde gange høyde.
bmi = round(weight/(height*height))
#Print setning med f-streng som forteller hvor mye BMIen til personen er.
print(f"da har du {bmi} i BMI.")