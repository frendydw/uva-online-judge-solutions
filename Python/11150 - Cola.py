# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 13:46:25 2021

@author: U540843
"""

while True:
    try:
        bottle = int(input())
        print(bottle + bottle//2)
        
    except EOFError:
        break