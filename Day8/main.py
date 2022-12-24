#IMPORT SEC
from tqdm import tqdm

#INPUT-HANDLING
with open("Day8/input.txt") as file:
    data = file.read().split('\n')
treemap = []
for el in range(len(data)):
    treemap.append([])
    for i in range(len(data[el])):
        treemap[el].append(int(data[el][i]))
        
def exploreTreemap(indice):
    element = treemap[indice[0]][indice[1]]
    if indice[0] == 0 or indice[1] == 0 or indice[0] == len(treemap)-1 or indice[1] == len(treemap[indice[0]])-1:
        return True
    line = treemap[indice[0]]
    column = [treemap[i][indice[1]] for i in range(len(treemap))]
    lbf = max([line[i] for i in range(0,indice[1])])
    laf = max([line[i] for i in range(indice[1]+1,len(line))])
    cbf = max([column[i] for i in range(0,indice[0])])
    caf = max([column[i] for i in range(indice[0]+1,len(column))])
    if (lbf) >= element and (laf) >= element and (cbf) >= element and (caf) >= element:
        return False
    else:
        return True
    
#PART-1
number = 0
for i in tqdm(range(len(treemap))):
    for j in range(len(treemap[i])):
        if exploreTreemap([i,j]):
            number += 1
print('PART-1: ',number)

#PART-2
def exploreTreemap2(indice):
    element = treemap[indice[0]][indice[1]]
    if indice[0] == 0 or indice[1] == 0 or indice[0] == len(treemap)-1 or indice[1] == len(treemap[indice[0]])-1:
        return 0
    line = treemap[indice[0]]
    column = [treemap[i][indice[1]] for i in range(len(treemap))]
    lbf = [line[i] for i in range(0,indice[1])]
    lbf = lbf[::-1]
    laf = [line[i] for i in range(indice[1]+1,len(line))]
    cbf = [column[i] for i in range(0,indice[0])]
    cbf = cbf[::-1]
    caf = [column[i] for i in range(indice[0]+1,len(column))]
    lb_viewdist = 1
    for count in range(len(lbf)):    
        if element > lbf[count]:
            lb_viewdist += 1
    la_viewdist = 1
    for count in range(len(laf)):    
        if element > laf[count]:
            la_viewdist += 1
    cb_viewdist = 1
    for count in range(len(cbf)):    
        if element > cbf[count]:
            cb_viewdist += 1
    ca_viewdist = 1
    for count in range(len(caf)):    
        if element > caf[count]:
            ca_viewdist += 1
    return lb_viewdist*ca_viewdist*la_viewdist*cb_viewdist

#PART-2
viewdists = []
for i in tqdm(range(len(treemap))):
    for j in range(len(treemap[i])):
        viewdists.append(exploreTreemap2([i,j]))
print('PART-2: ',max(viewdists))#284648
