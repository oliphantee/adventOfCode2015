f=open("day1.txt","r")

line=f.readline()
count=0
for i in range(len(line)):
    if line[i]=="(":
        count+=1
    elif line[i]==")":
        count-=1
        if count==-1:
            print(i+1) # part 2
            break
#print(count) # part 1
f.close()