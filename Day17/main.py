#IMPORT SECTION
import functools
import itertools
import support
from tqdm import tqdm
import sys
import math


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

#PART-2
# Read jet directions from input file
jet_directions = list(open('Day17/input.txt').read().strip())

# Convert jet directions to 1 (right) or -1 (left)
jet_directions = list(map(lambda _: -1 if _ == '<' else 1, jet_directions))

# Initialize solid squares and placed rocks
solid_squares = set([(x, 0) for x in range(7)])
placed_rocks = []

# Constants for rock spawn position
X_START_OFFSET = 2
Y_START_OFFSET = 4

# Patterns for different rock types
def spawn_rock(tower_height, pattern):
  # Bottom left coordinate
  x, y = (X_START_OFFSET, tower_height + Y_START_OFFSET)

  if pattern == 0:
    return set([
      (x, y),
      (x + 1, y),
      (x + 2, y),
      (x + 3, y)
    ])
  elif pattern == 1:
    return set([
      (x + 1, y),
      (x, y + 1),
      (x + 1, y + 1),
      (x + 2, y + 1),
      (x + 1, y + 2)
    ])
  elif pattern == 2:
    return set([
      (x, y),
      (x + 1, y),
      (x + 2, y),
      (x + 2, y + 1),
      (x + 2, y + 2)
    ])
  elif pattern == 3:
    return set([
      (x, y),
      (x, y + 1),
      (x, y + 2),
      (x, y + 3)
    ])
  elif pattern == 4:
    return set([
      (x, y),
      (x + 1, y),
      (x, y + 1),
      (x + 1, y + 1)
    ])

# Check if rock can fall
def should_fall(rock):
  for square in rock:
    x, y = square

    if (x, y - 1) in solid_squares:
      return False

  return True

# Make rock fall
def fall(rock):
  return set([(x, y - 1) for x, y in rock])

# Check if rock can be pushed
def should_push(rock, direction):
  for square in rock:
    x, y = square

    if direction == -1 and x - 1 < 0:
      return False
    
    if direction == 1 and x + 1 > 6:
      return False
    
    if (x + direction, y) in solid_squares:
      return False

  return True

# Push rock
def push(rock, direction):
  return set([(x + direction, y) for x, y in rock])

#define if the rock rest
def come_to_rest(rock):
    max_y = 0
    for square in rock:
        _, y = square
        solid_squares.add(square)
        max_y = max(max_y, y)
    placed_rocks.append(rock)
    return (max_y, rock)


def visualization(max_y = 10, min_y = 0, rock = set()):
  s = ''
  for y in range(max_y, min_y - 1, -1):
    for x in range(0,7):
      s += '@' if (x, y) in rock else '#' if (x, y) in solid_squares else '.'
    s += '\n'
  return s

def simulate(max_rocks):
  global tower_height
  global next_jet
  global next_rock
  global cycle_found

  for r in range(max_rocks):
    if not cycle_found:
      last_n_rocks = list(map(
        lambda rock: frozenset([(x, y - tower_height) for x, y in rock]),
        placed_rocks[-N_ROCKS_IN_STATE:]
      ))

      start_state = frozenset([
        next_jet,
        next_rock,
        frozenset(last_n_rocks)
      ])
      
      if start_state in seen_states:
        cycle_found = True
        r0, height0 = seen_states[start_state]

        cycle_length = r - r0
        height_per_cycle = tower_height - height0
        remaining_rocks = max_rocks - r0
        num_cycles = math.floor(remaining_rocks / cycle_length)

        r = r0 + (cycle_length * num_cycles)
        tower_height = height0 + (height_per_cycle * num_cycles)

        for rock in last_n_rocks:
          for x, y in rock:
            solid_squares.add((x, y + tower_height))

      else:
        seen_states[start_state] = (r, tower_height)

    rock = spawn_rock(tower_height, next_rock)

    while True:
      direction = jet_directions[next_jet]
    next_jet = (next_jet + 1) % len(jet_directions)
    if should_push(rock, direction):
      rock = push(rock, direction)
    if should_fall(rock):
      rock = fall(rock)
    else:
      break
  max_y, rock = come_to_rest(rock)
  tower_height = max(tower_height, max_y)
  next_rock = (next_rock + 1) % 5

ROCKS_TO_FALL = 1000000000000
N_ROCKS_IN_STATE = 30 # MAGIC NUMBER

next_jet = 0
next_rock = 0
tower_height = 0
seen_states = {}
cycle_found = False

# Calculate the number of full cycles in the simulation
full_cycles, remaining_rocks = divmod(ROCKS_TO_FALL, N_ROCKS_IN_STATE)

# Simulate the full cycles
simulate(full_cycles * N_ROCKS_IN_STATE)

# Simulate the remaining rocks
simulate(remaining_rocks)

print(tower_height)