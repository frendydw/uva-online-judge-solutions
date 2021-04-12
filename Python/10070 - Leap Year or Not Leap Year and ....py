test_no = 0
while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    if test_no > 0:
        print()
    
    flag = True
    
    if (n%4 == 0 and n%100 != 0) or (n%400 == 0):
        flag = False
        print("This is leap year.")
    if n%15 == 0:
        flag = False
        print("This is huluculu festival year.")
    if ((n%4 == 0 and n%100 != 0) or (n%400 == 0)) and n%55 == 0:
        flag = False
        print("This is bulukulu festival year.")
    if flag:
        print("This is an ordinary year.")
    
    test_no += 1