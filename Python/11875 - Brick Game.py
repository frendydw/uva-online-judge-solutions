import statistics
n = int(input())
index = 0

while n:
    arr = list(map(int, input().split()))
    del arr[0]
    print("Case {}: {}".format(index+1, statistics.median(arr)))
    index += 1
    n -= 1