seq = 1
while True:
    if seq > 1:
        print()
    flag = True
    n, m, c = map(int, input().split())
    
    if n == 0 and m == 0 and c == 0:
        break
    
    device = []
    sequence = []
    for i in range(n):
        d = int(input())
        device.append([d, "off"])
    for i in range(m):
        e = int(input())
        sequence.append(e)

    fuse = 0
    maxFuse = []
        
    for i in sequence:
        if device[i-1][1] == "off":
            fuse = fuse + device[i-1][0]
            maxFuse.append(fuse)
            device[i-1][1] = "on"
        else:
            fuse = fuse - device[i-1][0]
            device[i-1][1] = "off"
        
        if fuse > c:
            flag = False
            break
        
    print("Sequence {}".format(seq))
    if flag: 
        print("Fuse was not blown.")
        print("Maximal power consumption was {} amperes.".format(max(maxFuse)))
    else:
        print("Fuse was blown.")
    
    seq += 1