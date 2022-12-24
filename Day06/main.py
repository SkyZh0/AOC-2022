# Read input file
with open("Day06/input.txt") as file:
    data = file.read()

# PART 1
# Iterate through the data and find the first unique character sequence
for i in range(len(data) - 3):
    f, s, t, q = data[i], data[i+1], data[i+2], data[i+3]
    if len(set([f, s, t, q])) == 4:
        print(f"{i+1} = {f}, {i+2} = {s}, {i+3} = {t}, {i+4} = {q}")
        print(f"PART 1: {i+4}")
        break

# PART 2
# Iterate through the data and find the first unique character sequence
for i in range(len(data) - 13):
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 = data[i], data[i+1], data[i+2], data[i+3], data[i+4], data[i+5], data[i+6], data[i+7], data[i+8], data[i+9], data[i+10], data[i+11], data[i+12], data[i+13]
    if not any([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14].count(char) > 1 for char in [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14]):
        print(f"\n{i+1} = {c1}, {i+2} = {c2}, {i+3} = {c3}, {i+4} = {c4}, {i+5} = {c5}, {i+6} = {c6}, {i+7} = {c7}, {i+8} = {c8}, {i+9} = {c9}, {i+10} = {c10}, {i+11} = {c11}, {i+12} = {c12}, {i+13} = {c13}, {i+14} = {c14} \n PART-2 : {i+14}")
        break
