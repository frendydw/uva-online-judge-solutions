def sumOfDigits(num):
    num = str(num)
    
    if len(num) == 1:
        return int(num)
    return int(num[0]) + sumOfDigits(int(num[1:]))


while True:
    n = int(input())

    if n == 0:
        break
    
    m = n
    
    while m > 9:
        m = sumOfDigits(m)
        
    print(sumOfDigits(m))
        