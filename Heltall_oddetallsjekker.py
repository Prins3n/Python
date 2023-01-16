'''
Heltall/Oddetall sjekker
'''
#Ber brukeren om å skrive inn et heltall.
tall = int(input("Skriv et tall her: "))
#Variabel som bruker modulo operatoren for å finne ut om tallet blir 1 altså True eller 0 altså False.
sjekk = tall % 2
#If statement som sjekker om at hvis tallet blir 0, så er det et heltall.
if sjekk == False:
    #Print statement som kjører hvis tallet i variabelen tall 
    print("Dette er et heltall")
else:
    print("Dette er et oddetall")



'''
kan også gjøres på denne måten
bruk samme tall variabel

if tall % 2 == 0:
    print("Dette er et heltall")
else:
    print("Dette er et oddetall")
'''