inp = open('Day1/input.txt')
data = inp.read()
tolist = data.replace('\n',',').split(',')

final = []
temp = []
for i in tolist:
    if i != '':
        temp.append(int(i))
    else:
        final.append(temp)
        temp = []

sums = [sum(i) for i in final]
    
maxs = sorted(sums, reverse=True)[:3]
print('PART-1: ', maxs[0])
print('PART-2: ', sum(maxs))