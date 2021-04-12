def factor(num):
    total = 0
    for n in range(1, num):
        if num % n == 0:
            total += n
    return total


print('PERFECTION OUTPUT')
flag = True
while flag:
    arr = list(map(int, input().split()))
    for i in arr:
        if i == 0:
            flag = False
            break
        else:
            if factor(i) < i or i < 1:
                print('{:>5}  DEFICIENT'.format(i))
            elif factor(i) > i:
                print('{:>5}  ABUNDANT'.format(i))
            else:
                print('{:>5}  PERFECT'.format(i))
print('END OF OUTPUT')
