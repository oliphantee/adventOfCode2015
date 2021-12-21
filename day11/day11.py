initString="vzbxkghb"

def checkPassword(string):
    if "i" in string or "o" in string or "l" in string:
        return False
    first=False
    for i in range(len(string)-2):
        if ord(string[i])+2==ord(string[i+1])+1==ord(string[i+2]):
            first=True
            break
    if not first:
        return False
    i=0
    doubles=0
    doubleLetter=""
    while i<len(string)-1:
        if string[i]==string[i+1] and string[i]!=doubleLetter:
            doubles+=1
            doubleLetter=string[i]
            i+=2
        else:
            i+=1
    if doubles<2:
        return False
    return True

def increment(string):
    i=len(string)-1
    while string[i]=="z" and i>=0:
        string=string[:i]+"a"+string[i+1:]
        i-=1
    if i==-1:
        string="a"+string
    else:
        string=string[:i]+chr(ord(string[i])+1)+string[i+1:]
    return string

while not checkPassword(initString):
    initString=increment(initString)

print(initString)

string2=increment(initString)
while not checkPassword(string2):
    string2=increment(string2)

print(string2)