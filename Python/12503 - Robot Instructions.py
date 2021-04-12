# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:32:06 2021

@author: U540843
"""

n = int(input())

for i in range(n):
    m = int(input())
    count = 0
    arr = []
    for j in range(m):
        word = list(input().split())
        
        if word[0] == "RIGHT":
            arr.append(word)
            count += 1
        elif word[0] == "LEFT":
            arr.append(word)
            count -= 1
        else:
            arr.append(word)
            while word[0] == "SAME":
                temp = int(word[2]) -1
                word = arr[temp]
                if word[0] == "RIGHT":
                    count += 1
                elif word[0] == "LEFT":
                    count -= 1
        
    print(count)
