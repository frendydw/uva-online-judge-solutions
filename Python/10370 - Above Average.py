import statistics
n = int(input())
while n:
    above = 0
    arr = list(map(int, input().split()))
    del arr[0]
    avg = statistics.mean(arr)
    for f in arr:
        if f > avg:
            above += 1
        else:
            continue
    print("{0:.3f}%".format(above/(len(arr))*100))
    n -= 1