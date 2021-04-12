# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:28:32 2021

@author: U540843
"""

while True:
    start, first, second, third = map(int, input().split())
    
    deg = 360
    
    if start == 0 and first == 0 and second == 0 and third == 0:
        break
    print(1080 + ((start - first + 40) % 40 + (second - first + 40) % 40 + (second - third + 40) % 40) * 9)