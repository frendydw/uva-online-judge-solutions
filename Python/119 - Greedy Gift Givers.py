# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:35:11 2021

@author: U540843
"""

test_no = 0
while True:
    try:
        n = int(input())
        arrName = list(input().split())
        
        dictName = {}

        for i in arrName:
            dictName[i] = 0
            
        for i in range(n):
            arrList = list(input().split())
            
            if int(arrList[1]) > 0 and int(arrList[2]) > 0:
                gift = int(arrList[1]) // int(arrList[2])
                dictName[arrList[0]] -= gift*(len(arrList)-3)
                for i in range(3, len(arrList)):
                    key = arrList[i]
                    dictName[key] += gift

        if test_no > 0:
            print()
        for i in dictName:
            print(i, dictName[i])

        test_no += 1

    except EOFError:
        break
