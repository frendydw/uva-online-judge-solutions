while True:
    a, b = map(int, input().split())
    
    if a == -1 and b == -1:
        break
    
    res = max(a,b) - min(a,b)
    
    if res > 50:
        print(100-res)
    else:
        print(res)