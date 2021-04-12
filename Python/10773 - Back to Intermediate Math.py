import sys
from math import asin,tan
scan = lambda : sys.stdin.readline()

test = int(input())

for case in range(1, test+1):
    d, v, u = map(int, input().split())
    if u<=v or u==0 or v==0:
        print("Case %d: can't determine"%case)
    else:
        theta = asin(v/u)
        u1 = v/tan(theta)
        t1 = d/u1
        t2 = d/u
        print("Case %d: %.3f"%(case,t1-t2))