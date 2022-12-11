#IMPORT SEC
import typing
import functools

#INPUT HANDLING
with open('Day11/input.txt') as file:
    monkeys = file.read().split('\n\n')


#USEFULL FUNC
def square(x) -> int:
    return x*x

def multi(a, b) -> int:
    return a * b

def add(a, b) -> int:
    return a + b

#MONKEY DEF
class Monkey(typing.NamedTuple):
    items: list[int]
    fonc: typing.Callable[[int], int]
    modulo: int
    iftrue: int 
    iffalse: int 

#PART-1
monkeyz = []
for elt in monkeys:
    lines = elt.split('\n')
    starter = [int(s) for s in lines[1].split(': ')[1].split(', ')]
    if 'old * old' in lines[2]:
        fonc = square
    elif ' + ' in lines[2]:
        fonc = functools.partial(add, b=int(lines[2].split()[-1])) 
    elif ' * ' in lines[2]:
        fonc = functools.partial(multi, b=int(lines[2].split()[-1]))
    modulo = int(lines[3].split(' ')[-1])
    iftrue = int(lines[4].split(' ')[-1])
    iffalse = int(lines[5].split(' ')[-1])
    monkeyz.append(Monkey(starter, fonc, modulo, iftrue, iffalse))

rd = [0] * len(monkeyz)
for _ in range(20):
    for i, monkey in enumerate(monkeyz):
        for item in monkey.items:
            rd[i] += 1
            item = monkey.fonc(item) // 3
            if item % monkey.modulo == 0:
                monkeyz[monkey.iftrue].items.append(item)
            else:
                monkeyz[monkey.iffalse].items.append(item)
    monkey.items.clear()
rd.sort()

print('PART-1: ', seen[-1]*seen[-2])