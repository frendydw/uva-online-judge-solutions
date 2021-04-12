n = int(input())

while n:
    try:
        i, j = map(int, input().split())
    except EOFError:
        break
    
    if i < j:
        print('<')
    elif i > j:
        print('>')
    else:
        print('=')
    n -= 1