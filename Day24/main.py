#IMPORT SEC
import re
import collections
import support

#INPUT HANDLING
with open('Day24/input.txt') as file:
    data = file.read().split('\n')

#PART-1 --------------------
# Get start and target positions
sx, = (x for x, c in enumerate(data[0]) if c == '.')
sx = int(sx)
sx -= 1
sy = -1
tx, = (x for x, c in enumerate(data[-1]) if c == '.')
tx = int(tx)
tx -= 1
ty = len(data) - 3

# Extract the map from the input string
map_data = [line[1:-1] for line in data[1:-1]]
map_str = ''.join(map_data)

# Get the dimensions of the map
width = len(map_data[0])
height = len(map_data)

# Convert the map into a series of integer masks
up = tuple(int(re.sub('[^^]', '0', line).replace('^', '1')[::-1], 2) for line in map_data)
down = tuple(int(re.sub('[^v]', '0', line).replace('v', '1')[::-1], 2) for line in map_data)
left = tuple(int(re.sub('[^<]', '0', map_str[i::width]).replace('<', '1')[::-1], 2) for i in range(width))
right = tuple(int(re.sub('[^>]', '0', map_str[i::width]).replace('>', '1')[::-1], 2) for i in range(width))

# Initialize variables for breadth-first search
seen = set()
last = collections.deque([(0, sx, sy, up, down, left, right)])

# Perform breadth-first search
while last:
    depth, x, y, up, down, left, right = last.popleft()

    # Check if current position is blocked
    if y != -1 and (up[y] | down[y]) & (1 << x):
        continue
    elif y != -1 and (left[x] | right[x]) & (1 << y):
        continue
    # Check if current position is the target
    elif x == tx and y == ty:
        print('PART-1: ',depth + 1)
        break

    # Check if current position has been visited
    if (depth, x, y, up, down, left, right) in seen:
        continue
    else:
        seen.add((depth, x, y, up, down, left, right))

    # Generate next masks by shifting current masks
    next_masks = (
        up[1:] + (up[0],),
        (down[-1],) + down[:-1],
        left[1:] + (left[0],),
        (right[-1],) + right[:-1],
    )

    # Add "wait" move to queue
    last.append((depth + 1, x, y, *next_masks))

    # Add "move" moves to queue
    for (cx, cy) in support.adjacent_4(x, y):
        if 0 <= cx < width and 0 <= cy < height:
            last.append((depth + 1, cx, cy, *next_masks))


#PART-2 --------------------
# Get start and target positions
sx, = (x for x, c in enumerate(data[0]) if c == '.')
sx -= 1
sy = -1
tx, = (x for x, c in enumerate(data[-1]) if c == '.')
tx -= 1
ty = len(data) - 2

# Extract the map from the input string
map_lines = [line[1:-1] for line in data[1:-1]]
map_str = ''.join(map_lines)

# Get the dimensions of the map
width = len(map_lines[0])
height = len(map_lines)

# Convert the map into a series of integer masks
up = tuple(int(re.sub('[^^]', '0', line).replace('^', '1')[::-1], 2) for line in map_lines)
down = tuple(int(re.sub('[^v]', '0', line).replace('v', '1')[::-1], 2) for line in map_lines)
left = tuple(int(re.sub('[^<]', '0', map_str[i::width]).replace('<', '1')[::-1], 2) for i in range(width))
right = tuple(int(re.sub('[^>]', '0', map_str[i::width]).replace('>', '1')[::-1], 2) for i in range(width))

# Initialize variables for breadth-first search
seen = set()
last = collections.deque([(0, 0, sx, sy, up, down, left, right)])

# Perform breadth-first search
while last:
    tup = last.popleft()

    # Check if current position has been visited
    if tup in seen:
        continue
    else:
        seen.add(tup)

    depth, phase, x, y, up, down, left, right = tup

    # Check if current position is blocked
    if (x, y) != (sx, sy) and (x, y) != (tx, ty):
        if y != -1 and (up[y] | down[y]) & (1 << x):
            continue
        elif y != -1 and (left[x] | right[x]) & (1 << y):
            continue

    # Check if current position is the target
    if phase == 3 and (x, y) == (tx, ty):
        print('PART-2: ', depth)
        break

    # Generate next masks by shifting current masks
    next_masks = (
        up[1:] + (up[0],),
        (down[-1],) + down[:-1],
        left[1:] + (left[0],),
        (right[-1],) + right[:-1],
    )
    # Add "wait" move to queue
    last.append((depth + 1, phase, x, y, *next_masks))

    # Add "move" moves to queue
    for (cx, cy) in support.adjacent_4(x, y):
        if 0 <= cx < width and 0 <= cy < height:
            last.append((depth + 1, phase, cx, cy, *next_masks))
        elif phase == 0 and (cx, cy) == (tx, ty):
            last.append((depth + 1, 1, cx, cy, *next_masks))
        elif phase == 1 and (cx, cy) == (sx, sy):
            last.append((depth + 1, 2, cx, cy, *next_masks))
        elif phase == 2 and (cx, cy) == (tx, ty):
            last.append((depth + 1, 3, cx, cy, *next_masks))