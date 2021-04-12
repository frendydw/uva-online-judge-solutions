# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:02:39 2021

@author: U540843
"""

t = int(input())

for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    
    print((max(arr)-min(arr)) * 2)