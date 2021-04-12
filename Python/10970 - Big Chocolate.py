while True:
    
    try:
        m, n = map(int, input().split())
    except EOFError:
        break
    
    if m <= 1 and n <= 1:
        print(0)
    else:
        print(m*n-1)