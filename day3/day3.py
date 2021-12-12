f=open("day3.txt")

line=f.readline().rstrip()

locX=0
robX=0
robY=0
locY=0
visited={(0,0):1}
for i in range(len(line)):
    if line[i]=="^":
        if i%2==0:
            locY+=1
        else:
            robY+=1
    elif line[i]=="v":
        if i % 2 == 0:
            locY -= 1
        else:
            robY -= 1
    elif line[i]==">":
        if i % 2 == 0:
            locX += 1
        else:
            robX += 1
    else:
        if i % 2 == 0:
            locX -= 1
        else:
            robX -= 1
    if i%2==0:
        if (locX,locY) in visited:
            visited[(locX,locY)]+=1
        else:
            visited[(locX,locY)]=1
    else:
        if (robX,robY) in visited:
            visited[(robX,robY)]+=1
        else:
            visited[(robX,robY)]=1

print(len(visited))

f.close()