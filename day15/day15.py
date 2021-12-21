import numpy as np

f=open("day15.txt","r")

allIngred={}
ingredList=[]
for line in f.readlines():
    line=line.rstrip().replace(",","")
    name=line.split(": ")[0]
    ingredList.append(name)
    line=line.split()
    cap=int(line[2])
    dur=int(line[4])
    fla=int(line[6])
    tex=int(line[8])
    cal=int(line[10])
    allIngred[name]=(cap,dur,fla,tex,cal)

def getScore(allIngred,recipe):
    vals=[0,0,0,0,0]
    for key in recipe:
        for i in range(len(vals)):
            vals[i]+=recipe[key]*allIngred[key][i]
    calTot=vals[-1]
    vals=[max(i,0) for i in vals[:-1]]
    totScore=np.prod(vals)
    return totScore,calTot

maxScore=0
max2=0
for i in range(101):
    for j in range(101-i):
        for k in range(101-i-j):
            for l in range(101-i-j-k):
                recipe={ingredList[0]:i,ingredList[1]:j,ingredList[2]:k,ingredList[3]:l}
                score,cals=getScore(allIngred,recipe)
                if score>maxScore:
                    maxScore=score
                if cals==500 and score>max2:
                    max2=score
print(maxScore)
print(max2)

f.close()