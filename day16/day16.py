f=open("day16.txt","r")

facts={"children": 3,"cats": 7,"samoyeds": 2,"pomeranians": 3,"akitas": 0,"vizslas": 0,"goldfish": 5,"trees": 3,"cars": 2,"perfumes": 1}

for line in f.readlines():
    line=line.rstrip().split(", ")
    i=line[0].split(" ")[1].rstrip(":")
    line[0]=line[0].replace(":","&",1).split("&")[1].lstrip()
    correct1=True
    correct2=True
    for pair in line:
        pair=pair.rstrip(",").split(": ")
        if pair[0] in facts:
            if facts[pair[0]]!=int(pair[1]):
                correct1=False
        if pair[0] in facts:
            if pair[0] in ["cats","trees"]:
                if facts[pair[0]]>=int(pair[1]):
                    correct2=False
            elif pair[0] in ["pomeranians","goldfish"]:
                if facts[pair[0]]<=int(pair[1]):
                    correct2=False
            else:
                if facts[pair[0]]!=int(pair[1]):
                    correct2=False

    if correct1:
        print("part 1:",i)
    if correct2:
        print("part 2:",i)
f.close()