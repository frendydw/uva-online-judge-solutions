test_no = 0

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    if test_no > 0:
        print()
    for i0 in range(0, len(arr) - 5):
        for i1 in range(i0 + 1, len(arr) - 4):
            for i2 in range(i1 + 1, len(arr) - 3):
                for i3 in range(i2 + 1, len(arr) - 2):
                    for i4 in range(i3 + 1, len(arr) - 1):
                        for i5 in range(i4 + 1, len(arr)):
                            print(arr[i0], arr[i1], arr[i2], arr[i3], arr[i4], arr[i5])

    test_no += 1


