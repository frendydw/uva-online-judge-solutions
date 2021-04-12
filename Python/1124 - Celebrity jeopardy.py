# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:24:26 2021

@author: U540843
"""

while True:
    
    try:
        word = input()
    except EOFError:
        break
    
    print(word)