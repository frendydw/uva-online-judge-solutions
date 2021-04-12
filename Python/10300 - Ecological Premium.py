# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:43:43 2021

@author: U540843
"""

n = int(input())

for i in range(n):
    f = int(input())
    count = 0
    
    for i in range(f):
        a, b, c = map(int, input().split())
        
        if b > 0:
            count += a*c
    print(count)        
    