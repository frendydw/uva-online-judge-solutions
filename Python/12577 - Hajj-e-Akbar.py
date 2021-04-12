# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:53:06 2021

@author: U540843
"""

index = 1
while True:
    try:
        word = input()
    except EOFError:
        break
    
    if word == "*":
        break
    if word == "Hajj":
        print("Case {}: Hajj-e-Akbar".format(index))
    else:
        print("Case {}: Hajj-e-Asghar".format(index))
    index += 1