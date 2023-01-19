"Oppgave 3 modul 9"


"""

"""
csvFilepath = open("E:\OneDrive\Tisip\Python\Python Modul 9\kommuner.csv", "r")
jsonFilepath = open("E:\OneDrive\Tisip\Python\Python Modul 9\kommuner.json", "w")

import csv
import json

def valid_json_file(file):
    try:
        with open(file) as jsonfile:
            print(json.load(jsonfile))
    except TypeError:
        print("not a jsonfile.")

valid_json_file("test.json")