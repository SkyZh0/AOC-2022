file = open("Day3/input.txt")
data = file.read().split('\n')

bags = [[obj[0:(len(obj)-1)//2], obj[(len(obj)-1)//2:len(data)-1]] for obj in data]

common = []
for compart in bags:
    for item in compart[0]:
        if item in compart[1]:
            common.append(item)
        compart[0].replace(item,'')
print(common)
