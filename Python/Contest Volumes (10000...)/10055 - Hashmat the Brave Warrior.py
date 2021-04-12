while True:
    try:
        i, j = map(int, input().split())
    except EOFError:
        break
    
    print(abs(j - i))