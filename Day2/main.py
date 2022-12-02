"""

A = ROCK = X --> lose
B = PAPER = Y --> draw
C = SCISSORS = Z --> win

"""

file = open('Day2/input.txt')
data = file.read().split('\n')
data = [x.split(' ') for x in data]

winning = [['A','Y'],['B','Z'],['C','X']]
wpoints = [8,9,7]
loosing = [['A','Z'],['B','X'],['C','Y']]
lpoints = [3,1,2]
draw = [['A','X'],['B','Y'],['C','Z']]
dpoints = [4,5,6]

#PART-1
score = 0
for game in data:
    if game in winning:
        score += wpoints[winning.index(game)]
    elif game in loosing:
        score += lpoints[loosing.index(game)]
    elif game in draw:
        score += dpoints[draw.index(game)]

print('PART-1: ', score)

#PART-2
winnginstate = str([ord(x[1]) - 88 for x in data]).replace('0','lose').replace('1','draw').replace('2','win').split(', ')
winnginstate[0] = 'win'
winnginstate[2499] = 'lose'

hands = ['A','B','C']
wpoints2 = [8,9,7]
lpoints2 = [3,1,2]
dpoints2 = [4,5,6]
score2 = 0

for gameindex in range(len(data)):
    if winnginstate[gameindex] == 'win':
        score2 += wpoints2[hands.index(data[gameindex][0])]
    elif winnginstate[gameindex] == 'lose':
        score2 += lpoints2[hands.index(data[gameindex][0])]
    elif winnginstate[gameindex] == 'draw':
        score2 += dpoints2[hands.index(data[gameindex][0])]

print('PART-2: ', score2)
