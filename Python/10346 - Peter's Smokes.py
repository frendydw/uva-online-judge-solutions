def cal(n, k):
    if n == 0:
        return 0
    if n <= 1:
        return 1
    if n < k:
        return n
    return n + cal(n//k, k)
    
while True:
    try:
        n, k = map(int, input().split())
    except EOFError:
        break
        
    maxCig = n
    while n:
        if n == 0:
            break
        
        maxCig +=  n//k
        sisa = n - ((n//k)*k)
        n = sisa + n//k
        if n <= 1 or n < k:
            break
    print(maxCig)
    
