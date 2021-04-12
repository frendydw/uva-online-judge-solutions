import math

n = int(input())
wordList = []

for i in range(n):
    word = input()
    wordList.append(word)

song = ['Happy', 'birthday', 'to', 'you', 
        'Happy', 'birthday', 'to', 'you',
        'Happy', 'birthday', 'to', 'Rujia',
        'Happy', 'birthday', 'to', 'you']

loop = math.ceil(len(wordList) / len(song))
index = 0

for i in range(loop):
    for lyric in song:
        print("{}: {}".format(wordList[index], lyric))
        
        if index == len(wordList)-1:
            index = 0
        else:
            index += 1
        
            