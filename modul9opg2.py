"Oppgave 2 i modul 9"

import csv
import datetime

dato = datetime.date.today()
with open ("kommuner.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open ("kommunedatoer.csv", "w") as new_file:
        fieldnames = ['Kommunenummer', 'Kommunar']
        fieldnames.append(dato)
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=';')
        csv_writer.writeheader()
        
        for line in csv_reader:
            del line['Fylkesnummer']
            del line['Fylke']
            csv_writer.writerow(line)