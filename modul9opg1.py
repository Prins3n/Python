"Oppgave 1 i modul 9"


import csv

with open ("kommuner.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[2], line[3])