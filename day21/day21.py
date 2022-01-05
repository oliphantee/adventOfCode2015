import math as mt

bArm=2
bDmg=8

fweapons=open("weapons.txt","r")
fweapons.readline()

weapons=[]

for line in fweapons.readlines():
    line=line.split()
    weapons.append((int(line[1]),int(line[2])))

fweapons.close()

farmor=open("armor.txt","r")
farmor.readline()

armors=[(0,0)]

for line in farmor.readlines():
    line=line.rstrip().split()
    armors.append((int(line[1]),int(line[3])))

farmor.close()

frings=open("rings.txt","r")
frings.readline()

rings=[(0,0,0),(0,0,0)]

for line in frings.readlines():
    line=line.rstrip().split()
    rings.append((int(line[2]),int(line[3]),int(line[4])))

frings.close()

def fight(pArm,pDmg):
    global bDmg,bArm

    pHp = 100
    bHp = 109
    while (pHp and bHp)>0:
        bHp-=(max(1,pDmg-bArm))
        if bHp<=0:
            return True
            break
        pHp-=(max(1,bDmg-pArm))
        if pHp<=0:
            return False
            break
    print(pHp,bHp)

minCost=mt.inf
for weapon in weapons:
    for armor in armors:
        for ring1 in range(len(rings)):
            for ring2 in range(ring1+1,len(rings)):
                pArm=armor[1]+rings[ring1][2]+rings[ring2][2]
                pDmg=weapon[1]+rings[ring1][1]+rings[ring2][1]
                if fight(pArm,pDmg):
                    cost=weapon[0]+armor[0]+rings[ring1][0]+rings[ring2][0]
                    if cost<minCost:
                        minCost=cost

print(minCost) # part 1

maxCost=0
for weapon in weapons:
    for armor in armors:
        for ring1 in range(len(rings)):
            for ring2 in range(ring1+1,len(rings)):
                pArm=armor[1]+rings[ring1][2]+rings[ring2][2]
                pDmg=weapon[1]+rings[ring1][1]+rings[ring2][1]
                if not fight(pArm,pDmg):
                    cost=weapon[0]+armor[0]+rings[ring1][0]+rings[ring2][0]
                    if cost>maxCost:
                        maxCost=cost

print(maxCost) # part 2