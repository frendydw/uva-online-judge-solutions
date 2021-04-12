n = int(input())

for i in range(n):
    S = input()
    
    if S == '1' or S == '4' or S == '78':
        print("+")
    elif S[-2:] == '35':
        print("-")
    elif S[0] == '9' and S[-1] == '4':
        print("*")
    else:
        print("?")
