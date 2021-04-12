a = {}

def cal(x):
	if x in a:
		return a[x]
	
	if x <= 1:
		return 1
	
	if x % 2 == 1:
		y = 3 * x + 1
	else:
		y = x // 2
	
	a[x] = cal(y) + 1
	return a[x]


while True:
    try:
        i, j = map(int, input().split())
    except EOFError:
        break
    
    max_cycle = 0
    
    for n in range(min(i, j), max(i, j) + 1):
        count = cal(n)
			
        if count > max_cycle:
            max_cycle = count
            
    print(i, j, max_cycle)
