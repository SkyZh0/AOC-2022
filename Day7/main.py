#IMPORT-SEC
from collections import defaultdict
from typing import List

#PRELI
def inputh(lines: List[str]):
    disk = {}
    path = []
    p = 0
    while p < len(lines):
        line = lines[p].split()
        p += 1

        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    continue
                elif line[2] == "..":
                    if path:
                        path.pop()
                else:
                    path.append(line[2])

            elif line[1] == "ls":
                while p < len(lines):
                    line = lines[p].split()
                    p += 1

                    if line[0] == "$":
                        p -= 1
                        break
                    elif line[0] == "dir":
                        fullpath = "/".join([''] + path + [line[1]]) + "/"
                        disk[fullpath] = disk.get(fullpath, [])
                    else:
                        fullpath = "/".join([''] + path + [line[1]])
                        disk[fullpath] = int(line[0])

    return disk

def fsize(disk):
    files_only = {k:v for k,v in disk.items() if k[-1] != "/"}

    dsize = defaultdict(int)
    for filename, filesize in files_only.items():
        path = filename.split('/')[1:]
        while path:
            path.pop()
            fullpath = '/'.join(path)
            dsize[fullpath] += filesize

    return dsize

def sfilter(dsize):
    return {k:v for k,v in dsize.items() if v <= 100_000}


#PART-1
file = open("Day7/input.txt")
lines = [l.strip() for l in file]

disk = inputh(lines)
dsize = fsize(disk)
fdsize = sfilter(dsize)
result1 = sum(v for k,v in fdsize.items())

print(f'PART-1: {result1}')

#PART-2
space = 70000000
ndspace = 30000000
spspace = space - dsize['']
toErase = ndspace - spspace

for dir, size in sorted(dsize.items(), key=lambda x: x[1]):
    if size > toErase:
        print(f'PART-2: {dir}, {size}')
        break