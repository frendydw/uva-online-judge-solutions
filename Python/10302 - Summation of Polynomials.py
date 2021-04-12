# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:16:10 2021

@author: U540843
"""


while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    n = (n * n * (n + 1) * (n + 1)) // 4;
    print(n)