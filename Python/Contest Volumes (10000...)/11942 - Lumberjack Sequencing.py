n = int(input())

print("Lumberjacks:")
for i in range(n):
    arr = list(map(int, input().split()))
    
    flag = True
    
    if arr[0] < arr[-1]:
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                flag = False
                break
    else:
        for i in range(0, len(arr)-1):
            if arr[i] < arr[i+1]:
                flag = False
                break

    if flag:
        print("Ordered")
    else:
        print("Unordered")