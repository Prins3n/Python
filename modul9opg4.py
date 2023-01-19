


import json


def valid_json_file(file):
    try:
        with open(file) as jsonfile:
            print(json.load(jsonfile))
    except TypeError:
        print("not a jsonfile.")


valid_json_file("lonn.json")

with open("lonn.json") as jsonfile:
    data = json.load(jsonfile)


print(data["bedrift"]["ansatt"]["utbetalt"]["lonn"])