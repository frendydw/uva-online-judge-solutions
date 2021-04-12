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