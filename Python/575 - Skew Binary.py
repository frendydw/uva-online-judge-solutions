def sumOfDigits(num):
    num = str(num)
    skew = int(num) * (pow(2, len(num)) -1) 
    if len(num) == 1:
        return skew
    return int(num[0]) * (pow(2, len(num)) -1)  + sumOfDigits(int(num[1:]))

while True:
    n = int(input())
    if n == 0:
        break
    print(sumOfDigits(n))    
    