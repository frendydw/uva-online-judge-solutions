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
    
    index += 1
   
    print("Case {}: {}".format(index, paste))