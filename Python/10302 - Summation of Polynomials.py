while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    n = (n * n * (n + 1) * (n + 1)) // 4;
    print(n)