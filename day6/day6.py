import numpy as np

f=open("day6.txt","r")

lights=np.zeros((1000,1000))

for line in f.readlines():
    line=line.rstrip().split(" through ")
    lowBound=line[0].split()[-1].split(",")
    upBound=line[1].split(",")
    lowX=int(lowBound[0])
    lowY=int(lowBound[1])
    highX=int(upBound[0])
    highY=int(upBound[1])
    for i in range(lowX,highX+1):
        for j in range(lowY,highY+1):
            if "toggle" in line[0]:
                lights[i][j]+=2
            elif "off" in line[0]:
                lights[i][j]=max(0,lights[i][j]-1)
            else:
                lights[i][j]+=1

print(lights.sum())
f.close()