#INPUT HANDLING
file = open("Day6/input.txt")
data = file.read()
#PART-1
for i in range(len(data)):
    f,s,t,q = data[i],data[i+1],data[i+2],data[i+3]
    if not(f in (s,t,q)) and not(s in (f,t,q)) and not(t in (f,s,q)) and not(q in (f,s,t)):
        print(f" {i+1} = {f}, {i+2} = {s}, {i+3} = {t}, {i+4} = {q} \n PART-1 : {i+4}")
        break
#PART-2
for i in range(len(data)):
    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14 = data[i],data[i+1],data[i+2],data[i+3],data[i+4],data[i+5],data[i+6],data[i+7],data[i+8],data[i+9],data[i+10],data[i+11],data[i+12],data[i+13]
    if not(c1 in (c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14)) and not(c2 in (c1,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14)) and not(c3 in (c1,c2,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14)) and not(c4 in (c1,c2,c3,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14)) and not(c5 in (c1,c2,c3,c4,c6,c7,c8,c9,c10,c11,c12,c13,c14)) and not(c6 in (c1,c2,c3,c4,c5,c7,c8,c9,c10,c11,c12,c13,c14)) and not(c7 in (c1,c2,c3,c4,c5,c6,c8,c9,c10,c11,c12,c13,c14)) and not(c8 in (c1,c2,c3,c4,c5,c6,c7,c9,c10,c11,c12,c13,c14)) and not(c9 in (c1,c2,c3,c4,c5,c6,c7,c8,c10,c11,c12,c13,c14)) and not(c10 in (c1,c2,c3,c4,c5,c6,c7,c8,c9,c11,c12,c13,c14)) and not(c11 in (c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c12,c13,c14)) and not(c12 in (c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c13,c14)) and not(c13 in (c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c14)) and not(c14 in (c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13)):
        print(f"\n{i+1} = {c1}, {i+2} = {c2}, {i+3} = {c3}, {i+4} = {c4}, {i+5} = {c5}, {i+6} = {c6}, {i+7} = {c7}, {i+8} = {c8}, {i+9} = {c9}, {i+10} = {c10}, {i+11} = {c11}, {i+12} = {c12}, {i+13} = {c13}, {i+14} = {c14} \n PART-2 : {i+14}")
        break
