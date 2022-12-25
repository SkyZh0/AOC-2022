#IMPORT SECTION
import typing

#INPUT HANDLING
with open('Day18/input.txt') as f:
    obsi = {(int(x), int(y), int(z)) for x, y, z in [c.split(',') for c in f.read().split('\n')]}
    data = f.read().split('\n')
with open('Day18/input.txt') as f:
    data = f.read().split('\n')

#FUNCTION AND VARIABLES
def adjacent(
    x: int,
    y: int,
    z:int
) -> typing.Generator[tuple[int,int,int],None,None]:
    yield x + 1, y, z
    yield x - 1, y, z
    yield x, y + 1, z
    yield x, y - 1, z
    yield x, y, z + 1
    yield x, y, z - 1

#PART-1
count = 0
coords = set()

for line in data:
    x, y, z = map(int, line.split(','))
    count += 6
    for dx, dy, dz in adjacent(x, y, z):
        if (dx, dy, dz) in coords:
            count -= 2
    coords.add((x, y, z))

print('PART-1: ',count)

#PART-2
vsides = 0
voisins = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
seen = set()
queue = [(0, 0, 0)]

while queue:
    x,y,z = queue.pop(0)
    seen.add((x,y,z))
    for dx, dy, dz in voisins:
        bool = (x + dx, y + dy, z + dz)
        if -1 <= bool[0] <= 22 and -1 <= bool[1] <= 22 and -1 <= bool[2] <= 22 and bool not in seen and bool not in queue:
            if bool in obsi:
                vsides += 1
            else:
                queue.append(bool)

print('PART-2: ', vsides)