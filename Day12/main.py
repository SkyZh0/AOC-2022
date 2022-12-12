#IMPORT SEC
import support
import heapq

#INPUT HANDLING
with open('Day12/input.txt') as file:
    data = file.read().split('\n')

#PART-1
coords = {}
start = None
mapped = {
    'S' : chr(ord('a') - 1),
    'E' : chr(ord('z') + 1),
}

for y,line in enumerate(data):
    for x,c in enumerate(line):
        coords[(y,x)] = c
        if c == 'S':
            start = (y,x)
        elif c == 'E':
            end = (y,x)

visited = set()
left = [(0, start)]

while left:
    cost, pos = heapq.heappop(left)
    if pos == end:
        print('PART-1: ', cost-2)#339
    elif pos in visited:
        continue
    else:
        visited.add(pos)
    for cord in support.adjacent_4(*pos):
        if cord in coords:
            current = mapped.get(coords[pos], coords[pos])
            prox = mapped.get(coords[cord], coords[cord])
            if ord(prox) - ord(current) <= 1:
                heapq.heappush(left, (cost+1, cord))
            
#PART-2
coords = {}
for y,line in enumerate(data):
    for x,c in enumerate(line):
        coords[(y,x)] = c
        if c == 'E':
            end = (y,x)
visited = set()
left = [(0,end)]
while left:
    cost, pos = heapq.heappop(left)
    if coords[pos] == 'a':
        print('PART-2: ',cost-2)#332
        break
    elif pos in visited:
        continue
    else:
        visited.add(pos)
    for cord in support.adjacent_4(*pos):
        if cord in coords:
            current = mapped.get(coords[pos], coords[pos])
            prox = mapped.get(coords[cord], coords[cord])
            if ord(prox) - ord(current) >= -1:
                heapq.heappush(left, (cost+1, cord))