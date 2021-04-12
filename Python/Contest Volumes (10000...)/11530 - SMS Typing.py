index = 1

for n in range(int(input())):
    count = 0
    
    sentence = input()
    
    for i in range(len(sentence)):
        if (sentence[i] == "a" or sentence[i] == "d" or
            sentence[i] == "g" or sentence[i] == "j" or
            sentence[i] == "m" or sentence[i] == "p" or
            sentence[i] == "t" or sentence[i] == "w" or
            sentence[i] == " "):
            count += 1
        elif (sentence[i] == "b" or sentence[i] == "e" or
            sentence[i] == "h" or sentence[i] == "k" or
            sentence[i] == "n" or sentence[i] == "q" or
            sentence[i] == "u" or sentence[i] == "x"):
            count += 2
        elif (sentence[i] == "c" or sentence[i] == "f" or
            sentence[i] == "i" or sentence[i] == "l" or
            sentence[i] == "o" or sentence[i] == "r" or
            sentence[i] == "v" or sentence[i] == "y"):
            count += 3
        else:
            count += 4
    
    print("Case #{}: {}".format(index, count))
    index += 1