# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:57:05 2021

@author: U540843
"""


while True:
    try:
        n = int(input())
        p = int(input())
    except EOFError:
        break
    
    res = p**(1/n)
    
    print(round(res))