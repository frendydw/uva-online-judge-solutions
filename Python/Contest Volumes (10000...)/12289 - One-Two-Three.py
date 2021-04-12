n = int(input())
for i in range(n):
    word = input()
    count = 0
    
    if len(word) == 5:
        print('3')
        continue
    if word[0] == 'o':
        count += 1
    if word[1] == 'n':
        count += 1
    if word[2] == 'e':
        count += 1
        
    if count >= 2:
        print('1')
    else:
        print('2')