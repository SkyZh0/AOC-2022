#IMPORT SEC
import itertools
import ast
import functools

#INPUT HANDLING
with open('Day13/input.txt') as file:
    data = file.read()
Canva = int | list['Canva']

#FONCTIONS
def comparator(left: Canva, right: Canva) -> int:
    if isinstance(left, int) and not isinstance(right, int):
        left = [left]
    elif not isinstance(left, int) and isinstance(right, int):
        right = [right]
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, list) and isinstance(right, list):
        for a, b in itertools.zip_longest(left, right):
            if a is None:
                return -1
            elif b is None:
                return 1
            compared = comparator(a, b)
            if compared != 0:
                return compared
        else:
            return 0
    
#PART-1
lastval = 0
for i, stack in enumerate(data.split('\n\n'),1):
    sl1, sl2 = stack.split('\n')
    l1, l2 = ast.literal_eval(sl1), ast.literal_eval(sl2)
    if comparator(l1, l2) <= 0:
        lastval += i
print('PART-1: ',lastval)

#PART-2
data = data.replace('\n\n', '\n')
lists = [ast.literal_eval(line) for line in data.split('\n')]
lists.extend(([[2]],[[6]]))
lists.sort(key=functools.cmp_to_key(comparator))