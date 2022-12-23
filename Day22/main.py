#IMPORT SECTION
import re
import support

#INPUT HANDLING
with open('Day22/input.txt') as file:
    data = file.read()

#FUNCTIONS AND VARIABLES

#PART-1
maps, dirc = data.split('\n\n')
coords = {}

for y, line in enumerate(maps.splitlines()):
    for x, char in enumerate(line):
        if char == '.#':
            coords[(x, y)] = char
dy = [y for x,y in coords]
x = min(x for (x,y) in coords if y == 0)
y = min(dy) 
direx = support.Direction4.RIGHT

for elt in re.split('([RL])', dirc):
    if elt == 'R':
        direx = direx.cw 
    elif elt == 'L':
        direx = direx.ccw
    else:
        c = int(elt)
        for _ in range(c):
            director = direx.apply(x,y)
            if director not in coords:
                if direx is support.Direction4.RIGHT:
                    director_x = min(dx for (dx,dy) in coords if dy == y)
                    director = (director_x, y)
                elif direx is support.Direction4.LEFT:
                    director_x = max(dx for (dx,dy) in coords if dy == y)
                    director = (director_x, y)
                elif direx is support.Direction4.UP:
                    director_y = max(dy for (dx,dy) in coords if dx == x)
                    director = (x, director_y)
                elif direx is support.Direction4.DOWN:
                    director_y = min(dy for (dx,dy) in coords if dx == x)
                    director = (x, director_y)
            if coords[director] == '#':
                break
            else:
                x,y = director
possibles = {
    support.Direction4.RIGHT: 0,
    support.Direction4.DOWN: 1,
    support.Direction4.LEFT: 2,
    support.Direction4.UP: 3,
}

print('PART-1: ', 1000* (y+1) + 4* (x+1) + possibles[direx]) #127338 - INCORRECT

