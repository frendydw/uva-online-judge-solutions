# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:18:54 2021

@author: U540843
"""
count = 0

while True:
    try:
        word = input()
    except EOFError:
        break
    
    if word == "deadend":
        print(count)
        count = 0
    else:
        count += len(word)