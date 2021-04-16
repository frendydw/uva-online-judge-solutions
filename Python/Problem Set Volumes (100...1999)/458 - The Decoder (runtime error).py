while True:
    try:
        code = input()
    except EOFError:
        break
    if len(code) == 0:
        continue
    decode = ''
    for i in code:
        decode += chr(ord(i) - 7)

    print(decode)

