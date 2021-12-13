f=open("day8.txt","r")

count=0
total=0
count2=0
for line in f.readlines():
    total+=len(line.rstrip())
    line=line.rstrip()[1:-1]
    i=0
    count2+=6
    while i<len(line):
        if line[i]=="\\" and line[i+1]=="\\":
            i+=2
            count+=1
            count2+=4
        elif line[i]=="\\" and line[i+1]=='"':
            i+=2
            count+=1
            count2+=4
        elif line[i]=="\\" and line[i+1]=="x":
            i+=4
            count+=1
            count2+=5
        else:
            i+=1
            count+=1
            count2+=1

print(total-count) # part 1
print(count2-total) # part 2
f.close()