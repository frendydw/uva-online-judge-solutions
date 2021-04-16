case_no = 1
while True:
    A, limit = map(int, input().split())
    terms = 0
    temp_A = A
    if A < 0 and limit < 0:
        break

    while True:
        if A == 1:
            terms += 1
            break
        if A > limit:
            break
        elif A % 2 == 0:
            A = A//2
        elif A % 2 == 1:
            A = 3 * A + 1
        terms += 1

    print("Case {}: A = {}, limit = {}, number of terms = {}".format(case_no, temp_A, limit, terms))

    case_no += 1
