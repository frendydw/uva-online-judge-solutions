# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:53:38 2021

@author: U540843
"""

def sumOfDigits(num):
    num = str(num)
    
    if len(num) == 1:
        return int(num)
    return int(num[0]) + sumOfDigits(int(num[1:]))


while True:
    n = int(input())

    if n == 0:
        break
    
    m = n
    
    while m > 9:
        m = sumOfDigits(m)
        
    print(sumOfDigits(m))
        