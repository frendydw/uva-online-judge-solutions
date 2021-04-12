# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:06:44 2021

@author: U540843
"""

n = int(input())
index = 1

for i in range(n):
    x, y, z = map(int, input().split())
    
    temp = y + z
    
    while temp > x:
        temp = temp - x
        
    print("Case {}: {}".format(index, temp))
    index += 1