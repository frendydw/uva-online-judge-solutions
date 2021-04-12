# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:28:06 2021

@author: U540843
"""

case = 1

while True:
    try:
        zeros = input()
    except EOFError:
        break
        
    print("Case {}:".format(case))
    
    for x in range(int(input())):
        i, j = map(int, input().split())
        # flag = True
        
        # for t in range(min(i, j), max(i, j)):
        #     if zeros[t] != zeros[t+1]:
        #         flag = False
        #         break

        ra = zeros[min(i,j):max(i,j)+1]

        if zeros[min(i,j)] == "0":
            res = ra.find("1")
        else:
            res = ra.find("0")
        
        if res < 0:
            print("Yes")
        else:
            print("No")

    case += 1
   
    
    