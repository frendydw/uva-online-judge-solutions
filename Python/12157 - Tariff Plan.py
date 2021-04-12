# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:44:41 2021

@author: U540843
"""

n = int(input())
index = 1
for i in range(n):
    m = int(input())
    mile = 0
    juice = 0
    arr = list(map(int, input().split()))
    
    for i in arr:
        mi = i
        ju = i
        while mi >= 0:
            mile += 10
            mi -= 30
        while ju >= 0:
            juice += 15
            ju -= 60
           
    if mile == juice:
        print("Case {}: Mile Juice {}".format(index, mile))
    elif mile < juice:
        print("Case {}: Mile {}".format(index, mile))
    else:
        print("Case {}: Juice {}".format(index, juice))
        
    index += 1