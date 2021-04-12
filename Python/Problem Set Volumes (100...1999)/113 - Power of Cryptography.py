while True:
    try:
        n = int(input())
        p = int(input())
    except EOFError:
        break
    
    res = p**(1/n)
    
    print(round(res))
