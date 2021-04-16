for _ in range(int(input())):
    s, d = map(int, input().split())
    print('impossible' if (d > s or int(str((s-d)/2).split('.')[1]) > 0)
          else '{} {}'.format(int(s - ((s-d)/2)), int((s-d)/2)))
