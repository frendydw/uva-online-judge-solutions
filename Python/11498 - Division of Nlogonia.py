# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:13:52 2021

@author: U540843
"""

while True:
    n = int(input())
    if n <= 0:
        break
    x, y = map(int, input().split())
        
    for i in range(n):
        a, b = map(int, input().split())
        
        if a == x or b == y:
            print('divisa')
        elif a > x and b > y:
            print('NE')
        elif a < x and b < y:
            print('SO')
        elif a > x and b < y:
            print('SE')
        else:
            print('NO')