# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 00:18:42 2021

@author: U540843
"""

while True:
    
    try:
        a, b ,c , d = map(int, input().split())
    except EOFError:
        break
    
    flag = False
    ans = 0
    
    for i in range(c):
        e = int(input())
        f = list(map(int, input().split()))
        
        g = max(f)
        
        if a*e <= b:
             if g >= a:
                 flag = True
                 if ans == 0:
                     ans = a*e
                 elif a * e < ans:
                     ans = a*e
                 
    if flag:
        print(ans)
    else:
        print("stay home")
        
        