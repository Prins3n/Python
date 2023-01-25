from rot_codec import rot13_encode, rot13_decode
import random

with open("krypsitater.txt", "r") as f:
    r_sitat = f.read()
    s = r_sitat.split("%")
    tilfeldig = random.choice(s)
    print(rot13_decode(tilfeldig))