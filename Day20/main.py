#IMPORT SECTION
from unittest import mock
import support
import collections

#INPUT HANDLING
with open('Day20/input.txt') as file:
    data = file.read()

#PART-1
OGnums = support.parse_numbers_split(data)
nums = collections.deque(list(enumerate(OGnums)))

for i, number in enumerate(OGnums):
    id = nums.index((i, mock.ANY))
    nums.rotate(-id)
    nums.rotate(-number)
    nums.appendleft((i,number))
    
id0 = nums.index((mock.ANY, 0))
print(sum(
    nums[(id0 + i) % len(nums)][1]
    for i in (1000,2000,3000)
    ))


