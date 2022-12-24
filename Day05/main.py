import copy

#INPUT-HANDLING
crates = [
    ['---------------'],
    ['D','H','N','Q','T','W','V','B'], 
    ['D','W','B'], 
    ['T','S','Q','W','J','C'],
    ['F','J','R','N','Z','T','P'],
    ['G','P','V','J','M','S','T'],
    ['B','W','F','T','N'],
    ['B','L','D','Q','F','H','V','N'],
    ['H','P','F','R'],
    ['Z','S','M','B','L','N','P','H']]

crates2 = copy.deepcopy(crates)

file = open("Day05/input.txt")
data = file.read().split('\n')
moves = []
for i in range(len(data)):
    data[i] = data[i].split(' ')
for line in data:
    moves.append([line[1],line[3],line[5]])

#PART-1
def move(crates,mov):
    num,frm,to = int(mov[0]),int(mov[1]),int(mov[2])
    cratefrom = crates[frm]
    createto = crates[to]
    for i in range(num):
        temp = cratefrom[-1]
        cratefrom.remove(temp)
        createto.append(temp)
    return crates

def printcrates(crates):
    print('',crates[0],'\n',crates[1], '\n',crates[2], '\n',crates[3], '\n',crates[4], '\n',crates[5], '\n',crates[6], '\n',crates[7], '\n',crates[8],'\n',crates[9],'\n ----------------')

for m in moves:
    crates = move(crates,m)
    
print('PART-1:') 
printcrates(crates) #PSNRGBTFT

#PART-2
def move2(crate,move):
    cratefrom = crate[int(move[1])]
    createto = crate[int(move[2])]
    num = int(move[0])
    temp = cratefrom[len(cratefrom)-num:len(cratefrom)]
    for i in range(num):
        cratefrom.remove(temp[i])
        createto.append(temp[i])
    return crate

for mo in moves:
    crates2 = move2(crates2, mo)

print('PART-2:')
printcrates(crates2) #BNTZFPMMW