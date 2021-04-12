# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:58:04 2021

@author: U540843
"""

n = int(input())
index = 1

for i in range(n):
    arr = list(map(int, input().split()))
    del arr[0]
    result = max(arr)
    print("Case {}: {}".format(index, result))
    index += 1