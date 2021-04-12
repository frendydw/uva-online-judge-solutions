# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:19:20 2021

@author: U540843
"""

# =============================================================================
# def cal(n,i,paste):
#     if n == 1:
#         return 0
#     if i >= n:
#         return 1
#     return paste + cal(n,i,paste)
# =============================================================================

index = 0
while True:
    n = int(input())
    paste = 0
    i = 1
    if n < 0:
        break
    
    while True:
        if n == 1:
            paste = 0
            break
        paste += 1
        i = i*2
        if i >= n:
            break
    
    index+=1
   
    print("Case {}: {}".format(index, paste))