# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:02:06 2021

@author: U540843
"""
import statistics
index = 0
n = int(input())
while n:
    i, j, k = map(int, input().split())
    emp = (i,j,k)
    result = statistics.median(emp)
    print('Case {}: {}'.format(index+1, result))
    index += 1
    n -= 1