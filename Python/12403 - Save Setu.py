n = int(input())
K = 0
for i in range(n):
    try:
        word, donation = input().split(maxsplit=1)
        K = K + int(donation)
    except:
      print(K)
