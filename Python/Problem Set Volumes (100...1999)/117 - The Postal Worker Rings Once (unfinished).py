count = 0

while True:
    try:
        word = input()
    except EOFError:
        break
    
    if word == "deadend":
        print(count)
        count = 0
    else:
        count += len(word)