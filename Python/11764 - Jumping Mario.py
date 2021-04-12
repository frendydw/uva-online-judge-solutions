# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:58:12 2021

@author: U540843
"""

n = int(input())
index = 1

for i in range(n):
    jump = int(input())
    highJump = 0
    lowJump = 0
    
    arr = list(map(int, input().split()))
    
    for j in range(0, len(arr)-1):
        if arr[j] < arr[j+1]:
            highJump += 1
        elif arr[j] > arr[j+1]:
            lowJump += 1
    
    print("Case {}: {} {}".format(index, highJump, lowJump))
    index += 1