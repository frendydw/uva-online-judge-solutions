while True:
    n = int(input())
    if n == 0:
        break
    A = [x for x in range(1, n+1)]
    while True:
        B = list(map(int, input().split()))
        if B[0] == 0:
            break
        station = []
        flag = True
        in_count = 0
        out_count = 0

        while out_count < n:
            if in_count < n and A[in_count] == B[out_count]:
                in_count += 1
                out_count += 1
            elif len(station) > 0 and station[-1] == B[out_count]:
                station.pop()
                out_count += 1
            else:
                if in_count < n:
                    station.append(A[in_count])
                    in_count += 1
                else:
                    flag = False
                    break
        if flag:
            print('Yes')
        else:
            print('No')
    print()





