# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:16:43 2021

@author: U540843
"""

while True:
    try:
        i, j = map(int, input().split())
    except EOFError:
        break
    
    print(abs(j - i))