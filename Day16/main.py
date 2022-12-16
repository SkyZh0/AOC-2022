#IMPORT SEC
import re
import support
import itertools
import collections

#INPUT HANDLING
with open('Day16/input.txt') as file:
    data = file.read().split('\n')

#VARIABLES
flow = re.compile(r'rate=(\d+);')
valves = re.compile(r'to valves? (.*)$')

#PART-1
borders = {}
flows = {}
for line in data:
    _,name,*_ = line.split()
    compatible_valves = valves.search(line)
    targets = compatible_valves[1].split(', ')
    hit = flow.search(line)
    borders[name] = targets
    flows[name] = int(hit[1])

rate = frozenset(i for i,j in flows.items() if j)    
weight = {}
edges = ['AA',*rate]
for i,j in itertools.combinations(edges, r=2):
    todo: collections.deque[tuple[str, ...]]
    todo = collections.deque([(i,)])
    while todo:
        node = todo.popleft()
        if node[-1] == j:
            break
        else:
            todo.extend((*node,n) for n in borders[node[-1]])
    weight[(i,j)] = len(node)
    weight[(j,i)] = len(node)

#TIME TRAVEL
mini = -1
todo: list[tuple[int,int,tuple[str,...], frozenset[str]]]
todo = [(0,0,('AA',),rate)]
while todo:
    point, time, path, possible = todo.pop()
    mini = max(mini,point)
    
    for p in possible:
        ntime = time + weight[(path[-1],p)]
        if ntime < 30:
            todo.append((
                point + (30 - ntime) * flows[p],
                ntime,
                path + (p,),
                possible - {p},
            ))

print('PART-1: ',mini)


#PART-2
borders = {}
flows = {}
for line in data:
    _,name,*_ = line.split()
    compatible_valves = valves.search(line)
    targets = compatible_valves[1].split(', ')
    hit = flow.search(line)
    borders[name] = targets
    flows[name] = int(hit[1])

rate = frozenset(i for i,j in flows.items() if j)    
weight = {}
edges = ['AA',*rate]
for i,j in itertools.combinations(edges, r=2):
    todo: collections.deque[tuple[str, ...]]
    todo = collections.deque([(i,)])
    while todo:
        node = todo.popleft()
        if node[-1] == j:
            break
        else:
            todo.extend((*node,n) for n in borders[node[-1]])
    weight[(i,j)] = len(node)
    weight[(j,i)] = len(node)

#TIME TRAVEL
mini: dict[frozenset[str],int] = {}
todo: list[tuple[int,int,tuple[str,...], frozenset[str]]]
todo = [(0,0,('AA',),rate)]
while todo:
    point, time, path, possible = todo.pop()
    route = frozenset(path) - {'AA'}
    best = mini.setdefault(route, point)
    mini[route] = max(best,point)
    
    for p in possible:
        ntime = time + weight[(path[-1],p)]
        if ntime < 26:
            todo.append((
                point + (26 - ntime) * flows[p],
                ntime,
                path + (p,),
                possible - {p},
            ))

print('PART-2:', max(
    mini[i] + mini[j]
    for i,j in itertools.combinations(mini, r=2)
    if not i & j
))
