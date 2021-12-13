import itertools as iter
import math as mt

f=open("day9.txt","r")

allNodes={}
for line in f.readlines():
    line=line.rstrip().split(" = ")
    cost=int(line[1])
    line=line[0].split(" to ")
    start=line[0]
    end=line[1]
    if start in allNodes:
        allNodes[start][end]=cost
    else:
        allNodes[start]={end:cost}
    if end in allNodes:
        allNodes[end][start]=cost
    else:
        allNodes[end]={start:cost}

minCost=mt.inf
maxCost=0

for ordering in iter.permutations(allNodes.keys()):
    curCost=0
    prev=ordering[0]
    i=1
    while i<len(ordering):
        curCost+=allNodes[prev][ordering[i]]
        prev=ordering[i]
        i+=1
    if curCost<minCost:
        minCost=curCost
    if curCost>maxCost:
        maxCost=curCost

print(minCost) # part 1
print(maxCost) # part 2

f.close()