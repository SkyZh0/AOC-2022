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

sums = list()
for l in final:
    sums.append(sum(l))
    
maxi1 = max(sums)
sums.remove(maxi1)
maxi2 = max(sums)
sums.remove(maxi2)
maxi3 = max(sums)

print(maxi1,maxi2,maxi3)
print(maxi1+maxi2+maxi3)