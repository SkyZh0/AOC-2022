#INPUT HANDLING
file = open("Day03/input.txt")
data = file.read().split('\n')
#PART-1
bags = [[obj[0:((len(obj)-1)//2)+1], obj[((len(obj)-1)//2+1):len(data)-1]] for obj in data]
common,finalcommon = [],[]
for compart in bags:
    common.append(',')
    for item in compart[0]:
        if item in compart[1]:
            common.append(item)
        compart[0].replace(item,'')
common = (''.join(common)).split(',')
for item in common:
    finalcommon.append(''.join(set(item)))       
low, up, lowa, upa, sum= [i for i in range(1,27)], [i for i in range(27,53)], [chr(i) for i in range(97,123)], [chr(i) for i in range(65,91)], 0
for item in finalcommon:
    for char in item:
        if char.isupper():
            sum += up[upa.index(char)]
        else:
            sum += low[lowa.index(char)]
print('PART-1: ', sum)
#PART-2
groups = [[data[i],data[i+1],data[i+2]] for i in range(0,len(data)-2, 3)]
badge, finalbadge, sum = [], [], 0
for group in groups:
    badge.append(',')
    for char in group[0]:
        if char in group[1] and char in group[2]:
            badge.append(char)
badge = (''.join(badge)).split(',')
for item in badge:
    finalbadge.append(''.join(set(item)))
for badge in finalbadge:
    if badge.isupper():
        sum += up[upa.index(badge)]
    elif badge.islower():
        sum += low[lowa.index(badge)]
print('PART-2: ', sum)