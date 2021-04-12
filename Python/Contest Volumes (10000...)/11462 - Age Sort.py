# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:26:39 2021

@author: U540843
"""

while True:
    n = int(input())
    
    if n == 0:
        break
    
    arrAge = list(map(int, input().split()))
    
    arrAgeSort = sorted(arrAge)
    
    strAgeSort = ""
    
    for i in range(len(arrAgeSort)):
        if i == len(arrAgeSort)-1:
            strAgeSort += str(arrAgeSort[i])
        else:
            strAgeSort += str(arrAgeSort[i]) + " "
        
    print(strAgeSort)