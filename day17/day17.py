import math

f=open("day17.txt","r")

amtBought=150

allJugs=[]
for line in f.readlines():
    allJugs.append(int(line.rstrip()))

posAmts={(0,0):1}

for jug in allJugs:
    newAmts={}
    for key in posAmts:
        newAmts[key]=posAmts[key]
    for key in posAmts:
        if key[0]+jug<=amtBought:
            if (key[0]+jug,key[1]+1) in newAmts:
                newAmts[(key[0]+jug,key[1]+1)]+=posAmts[key]
            else:
                newAmts[(key[0] + jug, key[1] + 1)] = posAmts[key]
    posAmts=newAmts

tot150=0
minJugs=math.inf
for pos in posAmts:
    if pos[0]==amtBought:
        tot150+=posAmts[pos]
        if pos[1]<minJugs:
            minJugs=pos[1]
print(tot150) # part 1
print(posAmts[(amtBought,minJugs)]) # part 2