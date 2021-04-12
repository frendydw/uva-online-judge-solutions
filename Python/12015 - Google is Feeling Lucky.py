# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:48:09 2021

@author: U540843
"""

n = int(input())
index = 1

for i in range(n):
    res = {}
    arrNum = []
    for j in range(10):
        word, num = input().split()  
        if word in res and res[word] >= num:
            continue
        res[word] = num
        arrNum.append(int(num))
        
    key = str(max(arrNum))
    
    print("Case #{}:".format(index))
    for i in res:
        if key == res[i]:
            print(i)
    index+=1
