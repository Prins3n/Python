#importerer random modulen
import random

#åpner "sitater.txt" i "read-modus"
with open("sitater.txt", "r") as f:
    r_sitat = f.read()
    s = r_sitat.split("%")
    print(random.choice(s))
