# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:26:40 2021

@author: Anders
"""
"""Oppgave 2"""

"""TISIP har nylig utviklet et nytt elektronisk system der de vil kun ha 
små bokstaver i en tekstkommentarer på hva de liker med python 
og hva de syns er vanskelig med python. Etter en uke med brukertesting
 fant de ut at brukerne ikke skrev inn bare små bokstaver
 i det hele tatt, og det var veldig mange tilfeldige 
 og store bokstaver i teksten som ble sendt inn. 
 Et eksempel: 
	 «JEg sy25ns py10THen er et 23velDIg kjeKTt fag»,
 der det egentlig skal stå: 
	 «jeg syns python er et veldig kjekt fag».
 Lag en funksjon som fjerner alle tallene og store bokstaver fra teksten under
	 2.a«HvOR192for E2r fu89nkSJon23er S2å kje364kt?»
	  2.b«Hv820r M56789ye m9Å en 2345prograMM2345ERe 234for å3 b23li g4od9?»
	   2.c«6789Python09876 234er 234det 23kjekk345este pro2344grammer3ingsspråk2345et je23 vet9 9om»
 I denne oppgaven kreves det at du skriver minst én funksjon selv, og 
i tillegg benytterde vedlagte funksjonene.
 Husk at du kan kalle de vedlagte funksjonene inni funksjoner du skriver selv.
"""


def remove_numbers(text):
  new_string = "".join([i for i in text if not i.isdigit()]) 
  return new_string

def lower_case_text(text):
  return text.lower()

def away(text):	
	a = remove_numbers(text)
	b = lower_case_text(a)
	return b

print(away("HvOR192for E2r fu89nkSJon23er S2å kje364kt?"))
print(away("Hv820r M56789ye m9Å en 2345prograMM2345ERe 234for å3 b23li g4od9?"))
print(away("6789Python09876 234er 234det 23kjekk345este pro2344grammer3ingsspråk2345et je23 vet9 9om"))