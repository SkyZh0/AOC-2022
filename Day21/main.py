#IMPORT SECTION
import functools
import operator
import typing

#INPUT HANDLING
with open('Day21/input.txt') as file:
    data = file.read().splitlines()

#FUNCTIONS AND VARIABLES
operators = {
    '-': operator.sub,
    '+': operator.add,
    '/': lambda x, y: x//y,
    '*': operator.mul,
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


