f=open('day7.txt','r')

defined={}
failed=[]
prevFailed=0

def getVal(string):
    if string in defined:
        return defined[string]
    elif string.isdigit():
        return int(string)
    else:
        return None

def handleCmd(cmd,out,defined):
    global failed
    if len(cmd)==1:
        val=getVal(cmd[0])
        if val!=None:
            defined[out]=val
        else:
            failed.append((cmd,out))
    elif len(cmd)==2:
        val=getVal(cmd[1])
        if val!=None:
            defined[out]=65535-val
        else:
            failed.append((cmd,out))
    else:
        val1=getVal(cmd[0])
        val2=getVal(cmd[2])
        if val1!=None and val2!=None:
            if "OR" in cmd:
                defined[out]=val1|val2
            elif "AND" in cmd:
                defined[out]=val1&val2
            elif "RSHIFT" in cmd:
                defined[out]=val1>>val2
            elif "LSHIFT" in cmd:
                defined[out]=val1<<val2
        else:
            failed.append((cmd,out))
    return defined

for line in f.readlines():
    line=line.rstrip().split(" -> ")
    out=line[1]
    cmd=line[0].split()
    defined=handleCmd(cmd,out,defined)

while len(failed)!=prevFailed:
    prevFailed=len(failed)
    otherFailed=failed
    failed=[]
    for line in otherFailed:
        handleCmd(line[0],line[1],defined)
print(defined["a"])