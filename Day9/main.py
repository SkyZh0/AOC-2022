"""
     +y
      
 -x      +x
    
     -y
"""

#INPUT HANDLING
with open("Day9/input.txt") as file:
    moves = file.read().split('\n')
    moves = [elt.split(' ') for elt in moves]
    moves = [[elt[0], int(elt[1])] for elt in moves]

#PART-1
x,y = 0,0
movement = 0
for move in moves:
    if move[0] == 'U':
        y += move[1]
    elif move[0] == 'D':
        y -= move[1]
    elif move[0] == 'L':
        x -= move[1]
    elif move[0] == 'R':
        x += move[1]
    
    if abs(x) >= 1 and abs(y) > 1:
        while abs(x) >= 1 and abs(y) > 1:
            if x > 0 and y > 0:
                x -= 1
                y -= 1
                movement += 1
            elif x > 0 and y < 0:
                x -= 1
                y += 1
                movement += 1
            elif x < 0 and y > 0:
                x += 1
                y -= 1
                movement += 1
            elif x < 0 and y < 0:
                x += 1
                y += 1
                movement += 1
    if abs(y) >= 2 and abs(x) == 0:
        while abs(y) >= 2:
            if y > 0:
                y -= 1
                movement += 1
            else:
                y += 1
                movement += 1
    if abs(x) >= 2 and abs(y) == 0:
        while abs(x) >= 2:
            if x > 0:
                x -= 1
                movement += 1
            else:
                x += 1
                movement += 1

print(movement)