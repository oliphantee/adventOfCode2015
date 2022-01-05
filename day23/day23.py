f=open("day23.txt","r")

allLines=[]

for line in f.readlines():
    line=line.rstrip().split()
    if line[0]=="inc":
        allLines.append(line[1]+"+=1\ni+=1")
    elif line[0]=="hlf":
        allLines.append(line[1]+"/=2\ni+=1")
    elif line[0]=="tpl":
        allLines.append(line[1]+"*=3\ni+=1")
    elif line[0]=="jmp":
        allLines.append("i+="+line[1])
    elif line[0]=="jio":
        allLines.append("if "+line[1].rstrip(",")+"==1:\n\ti+="+line[2]+"\nelse:\n\ti+=1")
    elif line[0]=="jie":
        allLines.append("if "+line[1].rstrip(",")+"%2==0:\n\ti+="+line[2]+"\nelse:\n\ti+=1")

a=0
b=0
i=0

while i < len(allLines):
    exec(allLines[i])
print(b) # part 1

a=1
b=0
i=0

while i < len(allLines):
    exec(allLines[i])
print(b) # part 2