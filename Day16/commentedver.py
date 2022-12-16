import re # import the regular expression module
import support # import the support module (not defined in this code)
import itertools # import the itertools module
import collections # import the collections module

# INPUT HANDLING
with open('Day16/input.txt') as file:
    data = file.read().split('\n')

# VARIABLES
# compile regular expressions for extracting information from the input lines
flow = re.compile(r'rate=(\d+);') # extract the flow rate from the input line
valves = re.compile(r'to valves? (.*)$') # extract the names of the compatible valves from the input line

# PART-1
# create empty dictionaries to store the information extracted from the input lines
borders = {} # stores the names of the valves that each valve is connected to
flows = {} # stores the flow rate of each valve
# loop through each line of the input
for line in data:
    # split the line into words and assign the variables
    _,name,*_ = line.split() 
    # search for the compatible valves in the line using the valves regular expression
    compatible_valves = valves.search(line)
    # split the names of the compatible valves by ', ' to get a list of valve names
    targets = compatible_valves[1].split(', ')
    # search for the flow rate in the line using the flow regular expression
    hit = flow.search(line)
    # add the information to the dictionaries
    borders[name] = targets
    flows[name] = int(hit[1])

# create a frozenset of the names of the valves with non-zero flow rates
rate = frozenset(i for i,j in flows.items() if j)    
# create an empty dictionary to store the weights of the edges between valves
weight = {}
# create a list of the valve names that will be used as edges
edges = ['AA',*rate]
# loop through all pairs of edges
for i,j in itertools.combinations(edges, r=2):
    # create an empty deque (double-ended queue) to store the path to be explored
    todo: collections.deque[tuple[str, ...]]
    todo = collections.deque([(i,)])
    # loop until the deque is empty
    while todo:
        # get the first element in the deque
        node = todo.popleft()
        # check if the last element in the path is the destination valve
        if node[-1] == j:
            # if it is, exit the loop
            break
        else:
            # if it isn't, add the nodes that are connected to the current node to the deque
            todo.extend((*node,n) for n in borders[node[-1]])
    # add the length of the path to the dictionary of weights
    weight[(i,j)] = len(node)
    weight[(j,i)] = len(node)

# TIME TRAVEL (continued)
# initialize the minimum flow to -1
mini = -1
# create a list to store the states to be explored
# each state is represented as a tuple containing:
# - the current flow rate
# - the current time
# - the path of valves visited so far
# - the set of valves that have not yet been visited
todo = [(0,0,('AA',),rate)]
# loop until the list is empty
while todo:
    # pop the last state from the list
    point, time, path, possible = todo.pop()
    # update the minimum flow rate
    mini = max(mini,point)
    
    # loop through the valves that have not yet been visited
    for p in possible:
        # calculate the time required to reach the next valve
        ntime = time + weight[(path[-1],p)]
        # check if there is still time left to visit the valve
        if ntime < 30:
            # if there is, add the updated state to the list
            todo.append((
                point + (30 - ntime) * flows[p], # update the flow rate
                ntime, # update the time
                path + (p,), # update the path
                possible - {p}, # update the set of valves that have not yet been visited
            ))

# print the result of Part 1
print('PART-1: ',mini)
