# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:09:46 2021

@author: U540843
"""

n = int(input())
index = 1

for i in range(n):
    a,b,c = map(int, input().split())
    
    if a <= 20 and b <= 20 and c <= 20:
        print("Case {}: good".format(index))
    else:
        print("Case {}: bad".format(index))
        
    index += 1