"""
    A = ROCK = X --> lose
    B = PAPER = Y --> draw
    C = SCISSORS = Z --> win
"""
#INPUT HANDLING
file = open('Day02/input.txt')
data = file.read().split('\n')
data = [x.split(' ') for x in data]
#PART-1
winning, wpoints = [['A','Y'],['B','Z'],['C','X']], [8,9,7]
loosing, lpoints = [['A','Z'],['B','X'],['C','Y']], [3,1,2]
draw, dpoints = [['A','X'],['B','Y'],['C','Z']], [4,5,6]
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
winnginstate, winnginstate[0], winnginstate[2499] = str([ord(x[1]) - 88 for x in data]).replace('0','lose').replace('1','draw').replace('2','win').split(', '), 'win', 'lose'
hands, wpoints2, lpoints2, dpoints2 = ['A','B','C'], [8,9,7], [3,1,2], [4,5,6]
score2 = 0
for gameindex in range(len(data)):
    if winnginstate[gameindex] == 'win':
        score2 += wpoints2[hands.index(data[gameindex][0])]
    elif winnginstate[gameindex] == 'lose':
        score2 += lpoints2[hands.index(data[gameindex][0])]
    elif winnginstate[gameindex] == 'draw':
        score2 += dpoints2[hands.index(data[gameindex][0])]
print('PART-2: ', score2)
