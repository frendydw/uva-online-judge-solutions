fib = []
a, b = 0, 1

for i in range(5000):
    fib.append(b)
    a, b = b, a+b

while True:
    try:
        num = int(input())
        if num == 0:
            print('The Fibonacci number for 0 is 0')
        else:
            print('The Fibonacci number for {} is {}'.format(num, fib[num - 1]))
    except EOFError:
        break
