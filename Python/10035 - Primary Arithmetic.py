# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:07:37 2021

@author: U540843
"""        
    
while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    
    c = 0
    count = 0
    for i in range(10):
        c = a%10 + b%10 + c
        
        if c > 9:
            c = 1
        else:
            c = 0
        count += c
        a //= 10
        b //= 10
    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("{} carry operation.".format(count))
    else:
        print("{} carry operations.".format(count))
    
        