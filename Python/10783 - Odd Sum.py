index = 0
n = int(input())
while n:
    count = 0
    i = int(input())
    j = int(input())
    
    for k in range(i,j+1):
        if k%2 == 0:
            continue
        else:
            count += k
        k += 1
    print('Case {}: {}'.format(index+1, count))
    index += 1
        
    n -= 1