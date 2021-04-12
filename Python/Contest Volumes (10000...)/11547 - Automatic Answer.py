n = int(input())
while n:
    i = int(input())
    i = (((((i * 567)//9)+7492)*235)//47)-498
    print(abs(i)%100 // 10)
    n -= 1