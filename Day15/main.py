#IMPORT SEC
import re
from typing import NamedTuple

#INPUT HANDLING
with open('Day15/input.txt') as file:
    data = file.read().split('\n')

#PART 1
#USEFULL
regex = re.compile(
    r'^Sensor at x=(-?\d+), y=(-?\d+): '
    r'closest beacon is at x=(-?\d+), y=(-?\d+)$',
)

class Sensor(NamedTuple):
    x: int
    y: int 
    beacx: int 
    beacy: int 
    
    @property
    def distCalc(self) -> int:
        return abs(self.x - self.beacx) + abs(self.y - self.beacy)

#PART-1
beacs, coords = set(), set()
y = 2000000
for line in data:
    match = regex.match(line)
    sensor = Sensor(
        int(match[1]),int(match[2]),int(match[3]),int(match[4])
    )
    beacs.add((sensor.beacx, sensor.beacy))
    dist = sensor.distCalc
    rght = dist - abs(y - sensor.y)
    for x in range(sensor.x - rght, sensor.x + rght + 1):
        coords.add((x, y))
print('PART-1: ', len(coords-beacs))

#PART-2

