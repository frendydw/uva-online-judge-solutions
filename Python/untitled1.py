def sumOfDigits(num):
     num = str(num)
     if len(num) == 1:
         return int(num)
     return int(num[0]) + sumOfDigits(int(num[1:]))
     
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def sumNumberList(listNumber):
    if len(listNumber) == 1:
        return listNumber[0]
    else:
        return listNumber[0] + sumNumberList(listNumber[1:])
    
def fibonacci(num):
    if num == 0:
        return 0
    if num == 2 or num == 1:
        return 1
    return fibonacci(num-2) + fibonacci(num-1)
    
def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return a * power(a, b-1)
    
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
def dictionary(a, b):
    c = {}
    c[a] = 2 
    c[b] = 4
    print(c)
    
    