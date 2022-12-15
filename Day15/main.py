#IMPORT SEC
import re
from typing import NamedTuple
from typing import Any
from z3 import Optimize
from z3 import Int
from z3 import If
from z3 import sat

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
    
    def dist(self,x: int,y: int) -> int:
        return abs(self.x-x) + abs(self.y-y)
    
    @property
    def distCalc(self) -> int:
        return abs(self.x - self.beacx) + abs(self.y - self.beacy)

def absz(expression: Any) -> If:
    return If(expression >= 0, expression, -expression)

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
param = 4_000_000
opt = Optimize()
X = Int('X')
Y = Int('Y')
o.add(0 <= X)
o.add(0 <= Y)
o.add(X <= param)
o.add(Y <= param)
for line in data:
    match = regex.match(line)
    sensor = Sensor(
        int(math[1]), 
        int(math[2]), 
        int(math[3]), 
        int(math[4])    
        )
    o.add((absz(sensor.x - X) + absz(sensor.y - Y)) > sensor.distCalc)
result = o.model()
print(result[X].as_long() * param + result[Y].as_long())


                    