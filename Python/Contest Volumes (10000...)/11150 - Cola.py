while True:
    try:
        bottle = int(input())
        print(bottle + bottle//2)
        
    except EOFError:
        break