index = 0
while True:
    word = input()
    if (word == '#'):
        break
    if (word == 'HELLO'):
        print('Case {}: ENGLISH'.format(index+1))
    elif (word == 'HOLA'):
        print('Case {}: SPANISH'.format(index+1))
    elif (word == 'HALLO'):
        print('Case {}: GERMAN'.format(index+1))
    elif (word == 'BONJOUR'):
        print('Case {}: FRENCH'.format(index+1))
    elif (word == 'CIAO'):
        print('Case {}: ITALIAN'.format(index+1))
    elif (word == 'ZDRAVSTVUJTE'):
        print('Case {}: RUSSIAN'.format(index+1))
    else:
        print('Case {}: UNKNOWN'.format(index+1))
    index += 1