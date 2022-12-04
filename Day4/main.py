#INPUT HANDLING
file = open("Day4/input.txt")
data = file.read().split('\n')

spans = []
for tosplit in data:
    spans.append(tosplit.split(','))
    
for i in range(len(spans)):
    for j in range(len(spans[i])):
        spans[i][j] = spans[i][j].split('-')
        spans[i][j][0], spans[i][j][1] = int(spans[i][j][0]), int(spans[i][j][1])
        
for i in range(len(spans)):
    for j in range(len(spans[i])):
        spans[i][j] = [k for k in range(spans[i][j][0], spans[i][j][1]+1)]
        
#PART-1
result = 0
for span in spans:
    set1 = set(span[0])
    set2 = set(span[1])
    inter1 = set1.intersection(set2)
    inter2 = set2.intersection(set1)
    if inter1 == set2 or inter2 == set1:
        result += 1
print('PART-1: ',result)

#PART-2
result = 0
for span in spans:
    if any(item in span[0] for item in span[1]) or any(item in span[1] for item in span[0]):
        result += 1
print('PART-2: ',result)