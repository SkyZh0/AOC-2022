import support 
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
print('PART_1: ',sum(signal))
            
#PART-2 HARDER
pixels = set()
x = 1
stn, st = 0, 'noop'
lines = iter(data)

for i in range(1,241):
    if stn == 0:
        st = next(lines)
        if st == 'noop':
            stn = 1
        elif st.startswith('addx'):
            stn = 2
    stn -= 1

    if x-1 <= ((i-1)%40) <= x+1:
        pixels.add(((i-1)%40, (i-1)//40))
    
    if stn == 0:
        if st.startswith('addx'):
            addx, num = st.split(' ')
            x += int(num)
            
print('PART2: \n', support.format_coords_hash(pixels).replace(' ','.'))