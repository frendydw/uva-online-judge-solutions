def sumOfDigits(num):
    num = str(num)
    if len(num) == 1:
        return int(num)
    return int(num[0]) + sumOfDigits(int(num[1:]))
        

while True:
    n = int(input())
    if n == 0:
        break
    b = int(bin(n)[2:])
    
    print("The parity of {} is {} (mod 2).".format(b, sumOfDigits(b)))