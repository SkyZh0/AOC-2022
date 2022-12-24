#IMPORT SECTION
import functools
import itertools
import support
from tqdm import tqdm

#INPUT HANDLING
with open('Day17/input.txt') as file:
    data = file.read()

#PRELI
class Rock:
    def __init__(self, coords: set[tuple[int,int]]) -> None:
        self.coords = frozenset((x,-y) for x,y in coords)
        
    @functools.cached_property
    def height(self) -> int:
        miny = min(y for _, y in self.coords)
        maxy = max(y for _, y in self.coords)
        return maxy - miny + 1
    
    @functools.cached_property
    def width(self) -> int:
        minx = min(x for x, _ in self.coords)
        maxx = max(x for x, _ in self.coords)
        return maxx - minx + 1 
    
    def __hash__(self) -> int:
        return hash(seld.coords)
    
    def pos(self, dx: int, dy: int) -> set[tuple[int,int]]:
        return {(x+dx,y+dy) for x,y in self.coords}
        
STRPIECES = '''\
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
'''

PIECIES = tuple(
    Rock(support.parse_coords_hash(piece))
    for piece in STRPIECES.split('\n\n')
)

def formater(coords: set[tuple[int,int]]) -> str:
    minx = min(x for x,_ in coords)
    maxx = max(x for x,_ in coords)
    miny = min(y for _,y in coords)
    maxy = max(y for _,y in coords)
    return '\n'.join(
        ''.join(
            '#' if (x,y) in coords else ' '
            for x in range(minx,maxx + 1)
        )
        for y in range(maxy, miny - 1, -1)
    )

def printer(coords: set[tuple[int,int]]) -> None:
    print(formater(coords))

def movement(
    coords: set[tuple[int,int]],
    rock: Rock,
    x: int,
    y: int,
    direction: str,
) -> int:
    if direction == '<':
        if x == 0 or rock.pos(x-1, y) & coords:
            return x
        else:
            return x-1
    elif direction == '>':
        if x == rock.width - 1 or rock.pos(x+1, y) & coords:
            return x
        else:
            return x+1

#PART-1
data = data.strip()
piecies = itertools.cycle(PIECIES)
coords = support.parse_coords_hash('#######')
gas = itertools.cycle(data)
maxh = 0

for _ in tqdm(range(2022)):
    piece = next(piecies)
    x = 2
    y = maxh + piece.height + 3
    
    while True:
        x = movement(coords, piece, x, y, next(gas))
        if piece.pos(x,y-1) & coords:
            coords |= piece.pos(x,y)
            maxh = max(y for _,y in coords)
            break
        else:
            y -= 1
print('PART-1: ', max(y for _,y in coords))