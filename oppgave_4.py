

#importer rot13 algoritmen
from rot_codec import rot13_encode, rot13_decode

#åpner sitater tekst filen i read mode
with open("sitater.txt", "r") as r:
    #lager en ny tekst fil "kryptsitater" i write mode
    with open("krypsitater.txt", "w") as kw:
        #lager en variabel som leser "sitater.txt"
        content = r.read()
        #kw.write, altså den skriver ut innholdet i content variabelen som da er sitaterfilen og "encoder" innholdet.
        kw.write(rot13_encode(content))
