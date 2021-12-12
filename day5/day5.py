f=open("day5.txt","r")

count1=0
count2=0
for line in f.readlines():
    if "ab" not in line and "cd" not in line and "pq" not in line and "xy" not in line:
        nVowels=0
        prevC="\n"
        prev=False
        for c in line.rstrip():
            if c in "aeiou":
                nVowels+=1
            if c==prevC:
                prev=True
            prevC=c
        if nVowels>=3 and prev:
            count1+=1
    repDouble=False
    repOneSpace=False
    for i in range(len(line.rstrip())-1):
        if line[i:i+2] in line[i+2:]:
            repDouble=True
        if line[i]==line[i+2]:
            repOneSpace=True
    if repDouble and repOneSpace:
        count2+=1

print(count1)
print(count2)

f.close()