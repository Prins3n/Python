"""
Password Generator!
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passord = []

for characters in range(0, nr_letters):
    indexnr = random.randint(0, len(letters))
    characters = letters[indexnr -1]
    passord.append(characters)

for symbol in range(0, nr_symbols):
    indexnr1 = random.randint(0, len(symbols))
    symbol = symbols[indexnr1 -1]
    passord.append(symbol)

for number in range(0, nr_numbers):
    indexnr2 = random.randint(0, len(numbers))
    number = numbers[indexnr2 -1]
    passord.append(number)


random.shuffle(passord)
nytt_passord = "".join(passord)

print(nytt_passord)
