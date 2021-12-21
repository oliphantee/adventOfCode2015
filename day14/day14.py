f=open("day14.txt")

allReindeer=[]
for line in f.readlines():
    line=line.split()
    name=line[0]
    speed=int(line[3])
    dur=int(line[6])
    rest=int(line[13])
    allReindeer.append((name,speed,dur,rest))

def getPos(reindeer,t):
    name,speed,dur,rest=reindeer
    pos=t//(dur+rest)*(speed*dur) # distance travelled from complete cycles
    pos+=min(t%(dur+rest)*speed,dur*speed)
    return pos

maxDist=0
for reindeer in allReindeer:
    if getPos(reindeer,2503)>maxDist:
        maxDist=getPos(reindeer,2503)

print(maxDist) # part 1

allPoints={}
for t in range(1,2503):
    fastest=""
    furthest=0
    for reindeer in allReindeer:
        if getPos(reindeer,t)>furthest:
            furthest=getPos(reindeer,t)
            fastest=reindeer[0]
    if fastest in allPoints:
        allPoints[fastest]+=1
    else:
        allPoints[fastest]=1
print(allPoints) # part 2
f.close()