#IMPORT SECTION
import functools
import operator
import typing

import z3

#INPUT HANDLING
with open('Day21/input.txt') as file:
    data = file.read().splitlines()

#FUNCTIONS AND VARIABLES
operators = {
    '-': operator.sub,
    '+': operator.add,
    '/': lambda x, y: x/y,
    '*': operator.mul,
}

newOperators = {
    **operators,
    '/': lambda x, y: x//y
}

#PART-1
opes: dict[str, int | tuple[typing.Callable[[int, int], int], str, str]] = {}
for line in data:
    if len(line.split()) == 4:
        name, num = line.split(': ')
        ope1,ope,ope2 =num.split()
        opes[name] = (operators[ope],ope1,ope2)
    else:
        name, num = line.split(': ')
        opes[name] = int(num)

@functools.lru_cache
def value(name: str) ->int:
    val = opes[name]
    if isinstance(val, int):
        return val
    else:
        func, lft, rght = val
        return(func(value(lft),value(rght)))

print('PART-1: ',value('root'))

#PART-2 got an idea with z3
opti = z3.Optimize()
for line in data:
    if line.startswith('humn:'):
        continue
    elif line.startswith('root:'):
        _,x,_,y = line.split()
        opti.add(z3.Int(x) == z3.Int(y))
    elif len(line.split()) == 4:
        name, num = line.split(': ')
        ope1,ope,ope2 =num.split()
        opti.add(z3.Int(name) == operators[ope](z3.Int(ope1),z3.Int(ope2)))
    else:
        name, num = line.split(': ')
        opti.add(z3.Int(name) == int(num))

print('PART-2: ', opti.model()[z3.Int('humn')].as_long())

