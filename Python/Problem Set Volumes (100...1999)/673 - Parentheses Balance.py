for _ in range(int(input())):
    parentheses = input()
    flag = True
    check = []
    for _ in parentheses:
        if _ == '[' or _ == '(':
            check.append(_)
        elif _ == ']':
            if len(check) == 0 or check[-1] != '[':
                flag = False
                break
            check.pop()
        elif _ == ')':
            if len(check) == 0 or check[-1] != '(':
                flag = False
                break
            check.pop()

    print('Yes' if len(check) == 0 and flag else 'No')


