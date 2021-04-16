def cal(N):
    if N == 91:
        return N
    elif N >= 101:
        return cal(N-10)
    return cal(N+11)


while True:
    num = int(input())
    if num == 0:
        break
    print("f91({}) = {}".format(num, num-10) if num >= 101 else "f91({}) = {}".format(num, cal(num)))
