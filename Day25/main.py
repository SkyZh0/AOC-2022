#IMPORT SECTION
import math
from z3 import Int
from z3 import Optimize
from z3 import sat

#INPUT HANDLING
with open('Day25/input.txt') as file:
    data = file.read().split('\n')
    
#FUNCTIONS AND VARIABLES
REL = {
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '=',
}

#PART-1
def encode(k: int) -> str:
    retenue = ''
    while k:
        indic = k % 5
        if indic <= 2:
            retenue = retenue + str(indic)
        else:
            retenue = retenue + {3: '=', 4: '-'}[indic]
        k = k // 5
        k += indic // 3
    return retenue[::-1]


def main(data: str) -> int:
    retenue = 0
    for line in data:
        k = 0
        for i,char in enumerate(reversed(line)):
            if char.isdigit():
                k += int(char) * (5**i)
            elif char == '-':
                k -= 1 * (5**i)
            elif char == '=':
                k -= 2 * (5**i)
        retenue += k
    return retenue

print('PART-1: ',encode(main(data)))
        