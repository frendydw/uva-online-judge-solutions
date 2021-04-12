# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:02:05 2021

@author: U540843
"""

x = int(input())

for i in range(x):
    n, m = map(int, input().split())
    
    size = n * m
    
    row = m // 3
    column = n //3
    
    print(row * column)