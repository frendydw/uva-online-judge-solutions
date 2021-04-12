# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:56:12 2021

@author: U540843
"""

n = int(input())
index = 1

for i in range(n):
    arr = list(map(int, input().split()))
    
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]
    
    e1 = []
    small = min(arr[4], arr[5], arr[6])
    
    for i in range(4, 6):
        temp = 0
        if arr[i] < arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            i = 4
        
    e = ((arr[4] + arr[5])/2)
        
    result = a + b + c + d + e

        
    if result >= 90:
        print("Case {}: A".format(index))
    elif result >= 80:
        print("Case {}: B".format(index))
    elif result >= 70:
        print("Case {}: C".format(index))
    elif result >= 60:
        print("Case {}: D".format(index))
    else:
        print("Case {}: F".format(index))
    
    index += 1