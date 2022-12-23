import heapq

# Read input file and convert each line to a list of integers
with open('Day01/input.txt') as inp:
    final = [[int(x) for x in line.strip().split(',') if x.isdigit()] for line in inp]

# Find the 3 largest sums
sums = [sum(i) for i in final]
maxs = heapq.nlargest(3, sums)

# Output the results
print('PART-1: ', maxs[0], '\nPART-2: ', sum(maxs))
