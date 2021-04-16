test_no = 0
case = int(input())
for i in range(case):
    input()
    n = int(input())
    m = int(input())

    for ah in range(m):
        for j in range(1, n+1):
            print(''.join([str(j) for x in range(j)]))
        for k in reversed(range(1, n)):
            print(''.join([str(k) for x in range(k)]))
        if test_no == case-1 and ah == m-1:
            continue
        else:
            print()
    test_no += 1
