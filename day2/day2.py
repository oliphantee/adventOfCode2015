f=open("day2.txt","r")

def getCost(l,w,h):
    return 2*(l*h+l*w+w*h)+min([l*w,w*h,h*l]),min([2*l+2*w,2*w+2*h,2*h+2*l])+l*w*h

totCost=0
totRibbon=0
for line in f.readlines():
    line=line.rstrip().split("x")
    l,w,h=[int(i) for i in line]
    cost=getCost(l,w,h)
    totCost+=cost[0]
    totRibbon+=cost[1]

print(totCost) # part 1
print(totRibbon) # part 2
f.close()