# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:51:38 2021

@author: U540843
"""

n = int(input())
import math

for i in range(n):
    L = int(input())
    W = L * 0.6
    r = L * 0.2
    
    totalArea = L * W
    circleArea = (math.pi)*r*r
    squareArea = totalArea - circleArea
    
    print("{:.2f} {:.2f}".format(circleArea,squareArea))
    