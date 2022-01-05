import math
import queue

f=open("test2.txt","r")

allMappings={}
revMappings={}
for line in f.readlines():
    if "=>" in line:
        line=line.rstrip().split(" => ")
        if line[0] in allMappings:
            allMappings[line[0]].append(line[1])
        else:
            allMappings[line[0]]=[line[1]]
        if line[1] in revMappings:
            revMappings[line[1]].append(line[0])
        else:
            revMappings[line[1]]=[line[0]]
    elif len(line)>1:
        molecule=line.rstrip()

i=0
allPos=set()
allComps=[]
while i<len(molecule):
    curComp=molecule[i]
    start=i
    while i+1<len(molecule) and not molecule[i+1].isupper():
        curComp+=molecule[i+1]
        i+=1
    if curComp in allMappings:
        for repl in allMappings[curComp]:
            allPos.add(molecule[:start]+repl+molecule[i+1:])
    i+=1
    allComps.append(curComp)

costs={}
for val in allMappings["e"]:
    costs[val]=1

def getComps(string):
    allComps=[]
    for c in string:
        if c.isupper():
            allComps.append(c)
        else:
            allComps[-1]+=c
    return allComps

reached={}
reachedCosts={}
curQueue=queue.Queue()

curQueue.put((allComps,0))
while not curQueue.empty():
    curComps,curCost=curQueue.get()
    print(curCost,curComps)
    if curComps==["e"]:
        print(curCost)
    for i in range(len(curComps)-1):
        for j in range(i,min(i+10,len(curComps))):
            curStr="".join(curComps[i:j+1])
            print(curStr)
            if curStr in revMappings:
                for rev in revMappings[curStr]:
                    newStr="".join(curComps[:i]+[rev]+allComps[j+1:])
                    if newStr not in reachedCosts:
                        if rev!="e" or (i==0 and j==len(curComps)-1):
                            print("swapping {} for {} to make {}".format(curStr,rev,newStr))
                            curQueue.put((curComps[:i]+[rev]+allComps[j+1:],curCost+1))
                            reachedCosts[newStr]=curCost+1

print(reachedCosts)
print(reachedCosts["e"])

f.close() # part 2 is similar to the matrix multiplication problem I think. Probably feasible with an array instead of a dictionary