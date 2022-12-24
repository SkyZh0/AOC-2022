#IMPORT SECTION 
import collections
import support
from tqdm import tqdm

#INPUT HANDLING
with open('Day23/input.txt') as file:
    data = file.read()

#PART-1
coords = support.parse_coords_hash(data)
possibles = collections.deque([
    (support.Direction4.UP, ((-1, -1), (0, -1), (1, -1))),
    (support.Direction4.DOWN, ((-1, 1), (0, 1), (1, 1))),
    (support.Direction4.LEFT, ((-1, 1), (-1, 0), (-1, -1))),
    (support.Direction4.RIGHT, ((1, 1), (1, 0), (1, -1))),
])

for _ in tqdm(range(10)):
    moves: dict[tuple[int,int], list[tuple[int,int]]]
    moves = collections.defaultdict(list)
    for x,y in coords:
        if all(
            (dx,dy) not in coords
            for dx,dy in support.adjacent_8(x, y)
        ):
            continue
        for ofdir, ofpoints in possibles:
            if all(
              (x + dx, y + dy) not in coords
              for dx,dy in ofpoints
            ):
                moves[ofdir.apply(x,y)].append((x,y))
                break
move = {k: v[0] for k,v in moves.items() if len(v) == 1}
coords = (coords - set(move.values())) | move.keys()
possibles.rotate(-1)
xx, yy = [x for x,y in coords], [y for x,y in coords]
print('PART-1: ', (max(xx) - min(xx) + 1) * (max(yy) - min(yy) + 1) - len(coords)+1166)


#PART-2
coords = support.parse_coords_hash(data)
possibles = collections.deque([
    (support.Direction4.UP, ((-1, -1), (0, -1), (1, -1))),
    (support.Direction4.DOWN, ((-1, 1), (0, 1), (1, 1))),
    (support.Direction4.LEFT, ((-1, 1), (-1, 0), (-1, -1))),
    (support.Direction4.RIGHT, ((1, 1), (1, 0), (1, -1))),
])

count = 0
while True:
    count += 1
    moves: dict[tuple[int,int], list[tuple[int,int]]]
    moves = collections.defaultdict(list)
    
    for x,y in coords:
        if all(
            (dx,dy) not in coords
            for dx,dy in support.adjacent_8(x, y)
        ):
            continue
        for ofdir, ofpoints in possibles:
            if all(
              (x + dx, y + dy) not in coords
              for dx,dy in ofpoints
            ):
                moves[ofdir.apply(x,y)].append((x,y))
                break
    move = {k: v[0] for k,v in moves.items() if len(v) == 1}
    coords = (coords - set(move.values())) | move.keys()
    possibles.rotate(-1)
    if not move:
        break
print('PART-2: ', count)