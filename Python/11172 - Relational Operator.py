# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:29:01 2021

@author: U540843
"""
n = int(input())

while n:
    try:
        i, j = map(int, input().split())
    except EOFError:
        break
    
    if i < j:
        print('<')
    elif i > j:
        print('>')
    else:
        print('=')
    n -= 1