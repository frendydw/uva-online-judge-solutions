dictionary = {}

while True:
    arr = list(map(str, input().split()))
    if len(arr) == 0:
        break
    dictionary[arr[1]] = arr[0]


while True:
    try:
        word = input()
        print(dictionary[word] if word in dictionary else 'eh')
    except EOFError:
        break
