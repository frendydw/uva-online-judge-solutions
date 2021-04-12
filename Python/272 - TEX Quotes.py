# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:27:29 2021

@author: U540843
"""

flag = 1

while True:
    tempSentence = []
    try:
        sentence = input()
    except EOFError:
        break
    
    for char in sentence:
        if char == "\"":
            if flag == 1:
                tempSentence.append("``")
                flag = 2
            else:
                tempSentence.append("''")
                flag = 1
        else:
            tempSentence.append(char)
        
    print(''.join(tempSentence))