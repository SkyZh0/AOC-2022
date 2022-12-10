#INPUT HANDLING
with open('Day10/input.txt') as file:
    data = file.read().split('\n')

#PART 1
cycle, x, signal = 1,1, []
for line in data:
    #OPERATING
    if line == 'noop':
        cycle += 1
    if line.startswith('addx'):
        sline = line.split(' ')
        toadd = int(sline[1])
        x += toadd
        cycle += 2
    #CYCLE HANDLING
    if cycle in [20,60,100,140,180,220]:
        signal.append(cycle*x)
    if cycle in [21,61,101,141,181,221]:
        if line.startswith('addx'):
            sline = line.split(' ')
            tosub = int(sline[1])
            y = x - tosub
            signal.append((cycle-1)*y)
print(sum(signal))
            
    
