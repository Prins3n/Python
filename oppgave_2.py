with open("test2.txt", "r") as f:
    with open("testrev2.txt", "w") as w:
        w.write("".join(reversed(f.readlines())))