from itertools import permutations

f=open("day13.txt","r")

allPairs={}
allNames=set()
for line in f.readlines():
    line=line.rstrip(".\n")
    p1=line.split(" would ")[0] # person 1
    p2=line.split(" next to ")[-1] # person 2
    val=int(line.split()[3]) # happiness change
    if line.split()[2]=="lose": # handle reduction in happiness
        val*=-1
    allNames.add(p1)
    allNames.add(p2)
    if (p2,p1) in allPairs:
        allPairs[(p2,p1)]+=val
    else:
        allPairs[(p1,p2)]=val
def getMaxHap():
    maxHap=0
    for pos in permutations(allNames):
        totHap=0
        for i in range(-1,len(pos)-1):
            if (pos[i],pos[i+1]) in allPairs:
                totHap+=allPairs[(pos[i],pos[i+1])]
            else:
                totHap += allPairs[(pos[i+1], pos[i])]
        if totHap>maxHap:
            maxHap=totHap
    print(maxHap)
getMaxHap() # part 1

for name in allNames:
    allPairs[("Me",name)]=0
allNames.add("Me")
getMaxHap() # part 2