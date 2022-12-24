#IMPORT SECTION
import support

#INPUT HANDLING
with open("Day09/input.txt") as file:
    moves = file.read().split('\n')
    moves = [elt.split(' ') for elt in moves]
    moves = [[elt[0], int(elt[1])] for elt in moves]

#PARAMETERS
D = {
    'R': support.Direction4.RIGHT,
    'U': support.Direction4.UP,
    'L': support.Direction4.LEFT,
    'D': support.Direction4.DOWN,
}
headpos, tailpos = (0,0), (0,0)
visited = {tailpos}

#PART-1
for movement in moves:
    move = D[movement[0]]
    n = movement[1]
    for k in range(n):
        headpos = move.apply(*headpos)
        if abs(headpos[0]-tailpos[0]) >= 2 or abs(headpos[1]-tailpos[1]) >= 2:
            tailpos = move.opposite.apply(*headpos)
            visited.add(tailpos)
print('PART-1: ',len(visited))

#PART-2 -- -- -- -- --

#NEW-PARAMETERS
pos = [(0,0)]*10
visited2 = {pos[0]}

#FUNCTIONS
def mover(headpos,tailpos):
    hx,hy = headpos
    tx,ty = tailpos
    if abs(hy - ty) == 2 and abs(hx - tx) == 2:
        return ((hx + tx) // 2, (hy + ty) // 2)
    if abs(hy - ty) == 2:
        return (hx, (ty + hy) // 2)
    elif abs(hx - tx) == 2:
        return ((tx + hx) // 2, hy)
    else:
        return tailpos

#COMPUTING
for movement in moves:
    move = D[movement[0]]
    n = movement[1]
    for k in range(n):
        pos[0] = move.apply(*pos[0])
        previous = pos[0]
        for i in range(1,10):
            pos[i] = mover(previous, pos[i])
            previous = pos[i]
        visited2.add(pos[-1])
print('PART-2: ',len(visited2))