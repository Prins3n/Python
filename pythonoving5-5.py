# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 18:35:00 2021

@author: Anders
"""

def to_lister(x,y):
	for i in x:
		if i in y:
			return True
		else:
			return False

x = [1,2,3,4]
y = [1,4,5,6]

print(to_lister(x, y))