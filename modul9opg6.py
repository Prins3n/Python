"""
Modul 9 Oppgave 6
"""


import json

def valid_json_file(file):
    try:
        with open(file) as jsonfile:
            print(json.load(jsonfile))
    except TypeError:
        print("not a jsonfile.")

valid_json_file("tomtruise.json")

with open("tomtruise.json", "r") as jsonfile:
    source = jsonfile.read()

data = json.loads(source)
with open("actors.json", "w") as newfile:
    for i in data["Actors"]:
    
    newfile.write(data)
    