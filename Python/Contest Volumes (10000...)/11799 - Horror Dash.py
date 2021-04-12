n = int(input())
index = 1

for i in range(n):
    arr = list(map(int, input().split()))
    del arr[0]
    result = max(arr)
    print("Case {}: {}".format(index, result))
    index += 1