"Modul 9 opg 5"

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

for i in data["Actors"]:
    print(i["name"],i["wife"],i["children"])