while True:
    try:
        i, j = map(int, input().split())
    except EOFError:
        break
    
    print(2*j*i)