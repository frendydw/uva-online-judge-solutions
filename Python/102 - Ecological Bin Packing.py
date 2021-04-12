while True:
    try:
        arr = list(map(int, input().split()))
    except EOFError:
        break
    
    bin1 = arr[0:3]
    bin2 = arr[3:6]
    bin3 = arr[6:9]
    
    count1 = bin2[0] + bin3[0] + bin1[1] + bin3 [1] + bin1[2] + bin2[2] 
    count2 = bin2[0] + bin3[0] + bin1[2] + bin3 [2] + bin1[1] + bin2[1] 
    count3 = bin2[1] + bin3[1] + bin1[0] + bin3 [0] + bin1[2] + bin2[2] 
    count4 = bin2[1] + bin3[1] + bin1[2] + bin3 [2] + bin1[0] + bin2[0] 
    count5 = bin2[2] + bin3[2] + bin1[1] + bin3 [1] + bin1[0] + bin2[0]
    count6 = bin2[2] + bin3[2] + bin1[0] + bin3 [0] + bin1[1] + bin2[1] 

    minCount = min(count1, count2, count3, count4, count5, count6)

    if minCount == count2:
        print('BCG', count2)
    elif minCount == count1:
        print('BGC', count1)
    elif minCount == count6:
        print('CBG', count6)
    elif minCount == count5:
        print('CGB', count5)
    elif minCount == count3:
        print('GBC', count3)
    elif minCount == count4:
        print('GCB', count4)
