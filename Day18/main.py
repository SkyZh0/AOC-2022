#IMPORT SECTION
import typing

#INPUT HANDLING
with open('Day18/input.txt') as file:
    data = file.read().split('\n')

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