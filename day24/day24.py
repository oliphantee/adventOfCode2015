import math as mt
import numpy as np
import random as rd
import functools as ft

f=open("day24.txt","r")

allPkgs=[]
for line in f.readlines():
    allPkgs.append(int(line.rstrip()))

thirdWeight=sum(allPkgs)/4
# allPkgs=allPkgs[::-1]
# print(thirdWeight)
# possibleConfigs=[(0,[])]
# defPossible=[]
# minLen=mt.inf
# minProd=mt.inf
# for i in range(len(allPkgs)):
#     newPossible=[]
#     for possible in possibleConfigs:
#         if possible[0]+allPkgs[i]<=520 and len(possible)<minLen:
#             newPossible.append((possible[0]+allPkgs[i],possible[1]+[allPkgs[i]]))
#             newPossible.append(possible)
#         elif possible[0]==520 and len(possible[1])<=minLen:
#             #print(possible)
#             if len(possible[1])<minLen:
#                 minLen=len(possible[1])
#                 minProd=np.prod(possible[1])
#                 print(possible[1])
#             elif minLen==len(possible[1]):
#                 minProd=np.prod(possible[1])
#                 print(possible[1])
#     print(len(newPossible),minLen,minProd)
#     possibleConfigs=newPossible
# print(len(possibleConfigs))

def stabilize(grps):
    changed=True
    while changed:
        changed=False
        for i in range(len(grps)):
            for j in range(len(grps)):
                if sum(grps[i])>sum(grps[j]):
                    ind=rd.choice(range(len(grps[i])))
                    grps[j].append(grps[i].pop(ind))
                    changed=True
    return grps

minLen=mt.inf
minGrps=[]
for t in range(100):
    grps=[[],[],[],[]]
    for i in range(len(allPkgs)):
        grp=rd.choice([0,1,2,3])
        grps[grp].append(allPkgs[i])
    grps=stabilize(grps)
    grps.sort(key=len)
    if len(grps[0])<minLen:
        minLen=len(grps[0])
        grps[0].sort()
        minGrps=[grps[0]]
    elif len(grps[0])==minLen:
        grps[0].sort()
        if grps[0] not in minGrps:
            minGrps.append(grps[0])
    if t%10==0:
        minGrps.sort(key=lambda a: ft.reduce(lambda c,d:c*d,a))
        minGrps=[minGrps[0]]
        print(t)

print(len(minGrps))
print(minGrps)
minGrps.sort(key=lambda a: ft.reduce(lambda c,d:c*d,a))
print(ft.reduce(lambda c,d:c*d,minGrps[0]))