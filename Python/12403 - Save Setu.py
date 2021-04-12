# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:42:52 2021

@author: U540843
"""

n = int(input())
K = 0
for i in range(n):
    try:
        word, donation = input().split(maxsplit=1)
        K = K + int(donation)
    except:
      print(K)