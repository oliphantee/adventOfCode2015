f=open("day18.txt","r")

T_MAX=100
SIZE=100

def getNeighbors(i,j,maxRow,maxCol):
    nList=[]
    if i==0:
        rows=[i,i+1]
    elif i==maxRow:
        rows=[i-1,i]
    else:
        rows=[i-1,i,i+1]
    if j==0:
        cols=[j,j+1]
    elif j==maxCol:
        cols=[j-1,j]
    else:
        cols=[j-1,j,j+1]
    for k in rows:
        for l in cols:
            nList.append((k,l))
    return nList

allOn=set()
i=0
for line in f.readlines():
    for j in range(len(line)):
        if line[j]=="#":
            allOn.add((i,j))
    i+=1

for t in range(T_MAX):
    newOn=set()
    for i in range(SIZE):
        for j in range(SIZE):
            count=0
            for nLoc in getNeighbors(i,j,SIZE-1,SIZE-1):
                if nLoc in allOn:
                    count+=1
            if count==3 or (count==4 and (i,j) in allOn):
                newOn.add((i,j))
    newOn.add((0,0)) # remove the following four lines for part 1
    newOn.add((0,SIZE-1))
    newOn.add((SIZE-1,0))
    newOn.add((SIZE-1,SIZE-1))
    allOn=newOn

print(len(allOn))
f.close()