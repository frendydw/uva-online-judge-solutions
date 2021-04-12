while True:
    
    try:
        word = input()
    except EOFError:
        break
    
    print(word)