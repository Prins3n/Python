# coding=utf-8
"Fizzbuzz game"
#lagte noen variabler bare for gøy så eg slapp å skriva så mye seinere.
f = "Fizz"
b = "Buzz"

#forløkke som traversere tallene fra 0 te 100 og øke med ein kver gang. Heilt unnødvendigt å ha et 1 tall der på slutten egentlig men fuck it.
for number in range(0,101, 1):
    #liden variabel som seie at "value" valuen e 0 grunnen te eg gjorde dette va sånn at tallet alltid skulle gå tebage te 0 siden det plussa seg sammen. kunne egentlig fjerna valuene.
    value = 0
    #liden variabel som legge te nummeret te value. måtte ha den over siden eg hadde denne. kunne nok fjerna begge. uten at det hadde gjort særlig skade, men forstår koden lettere då.
    value += number
    #liden if som seie at hvis elementet i rangen kan delas på 3 og bli 0 OG elementet i rangen kan deles på 5 og bli 0 gjør dette.
    if number % 3 == 0 and number % 5 == 0:
        print(f+b)
    #liden elif som seie at hvis elementet i rangen e delelikt på 5 og blir 0 så ska me printa b som e buzz.
    elif number % 5 == 0:
        print(b)
    #liden elif som seie at hvis elementet i rangen e delelikt på 3 og blir 0 så ska me printa f som e Fizz.
    elif number % 3 == 0:
        print(f)
    #liden else som seie ellers så ska me bare printa value som vil sei nummeret for kver gang loopen kjøre.
    else:
        print(value)