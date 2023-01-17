#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:51:22 2021

@author: andersgrondahl
"""

def calculate_size(length, height, width):
  return length*height*width

pool1 = calculate_size(10, 15, 20)
pool2 = calculate_size(20, 8, 20)
pool3 = calculate_size(10, 25, 15)

if pool1 > pool2 and pool3:
    print("De bør velge det første bassenget siden det har et volum på", pool1)
elif pool2 > pool3:
    print("De bør velge det andre bassenget siden det har et volum på", pool2)
else:
    print("De bør velge det siste bassenget siden det har et volum på", pool3)
