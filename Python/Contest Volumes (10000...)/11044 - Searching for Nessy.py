x = int(input())

for i in range(x):
    n, m = map(int, input().split())
    
    size = n * m
    
    row = m // 3
    column = n //3
    
    print(row * column)