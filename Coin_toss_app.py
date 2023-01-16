"""
Welcome to the Coin Toss application.
"""
#importerer random modulen, slik at vi enkelt kan få et tilfeldig tall.
import random
#variabel som sier at variabelen skal hente et integer mellom 0 og 1.
random_integer = random.randint(0,1)
#if setning som sier at hvis tallet variabelen skaper er 1 gjør følgende.
if random_integer == 1:
    print("You flipped the coin and it landed on Heads.")
#hvis tallet ikke er 0 skal else statementen gjøre følgende.
else:
    print("Tails, unfortunately you lost.")