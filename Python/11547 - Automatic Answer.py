# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:13:55 2021

@author: U540843
"""

n = int(input())
while n:
    i = int(input())
    i = (((((i * 567)//9)+7492)*235)//47)-498
    print(abs(i)%100 // 10)
    n -= 1