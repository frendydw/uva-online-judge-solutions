import math

while True:
    i, j, k = map(int, input().split())
    if i == 0 and j == 0 and k == 0:
        break
    result = math.sqrt(i**2 + j**2)
    
    if k == math.sqrt(i**2 + j**2) or j == math.sqrt(i**2 + k**2) or i == math.sqrt(j**2 + k**2):
        print('right')
    else:
        print('wrong')
    