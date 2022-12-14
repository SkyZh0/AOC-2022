#IMPORT SEC
import support
#INPUT HANDLING
with open('Day14/input.txt') as file:
    data = file.read()

#PART-1
SAND = (500,0)
coords = set()
for line in data.split('\n'):
    points = line.split(' -> ')
    bfx,bfy = support.parse_numbers_comma(points[0])
    for point in points[1:]:
        cux,cuy = support.parse_numbers_comma(point)
        if cux == bfx:
            for y in range(min(cuy,bfy),max(cuy,bfy)+1):
                coords.add((cux,y))
        else:
            for x in range(min(cux,bfx),max(cux,bfx)+1):
                coords.add((x,cuy))
        bfx, bfy = cux, cuy
maxi = max(y for _, y in coords)

count = 0
BOOL = True
while BOOL:
    x,y = 500, 0
    while True:
        if (x,y+1) not in coords:
            y += 1
        elif (x-1,y+1) not in coords:
            x -= 1
            y += 1
        elif (x+1,y+1) not in coords:
            x += 1
            y += 1
        else:
            coords.add((x,y))
            break
        if y > maxi:
            print('Part-1: ', count)
            BOOL = False
            break
    count += 1
