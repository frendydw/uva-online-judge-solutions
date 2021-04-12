for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    swap = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap += 1

    print("Optimal train swapping takes {} swaps.".format(swap))