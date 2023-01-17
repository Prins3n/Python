#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:46:30 2021

@author: andersgrondahl
"""


def to_lister(x, y): #lager en funksjon som tar inn to lister som inn parametere
    for i in x:
        if i not in y:
            sammen = set(x) ^ set(y)
    return sammen

x = [1, 2, 3, 5]
y = [1, 4, 4, 6]

print(to_lister(x, y))