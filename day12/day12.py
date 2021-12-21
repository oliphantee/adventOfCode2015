f=open("day12.txt","r")

class ListNode:
    def __init__(self):
        self.vals=[]
        self.parent=None

    def getSum(self,noRed=False):
        totSum = 0
        for val in self.vals:
            if type(val) == int:
                totSum += val
            elif type(val)==ListNode or type(val)==DictNode:
                totSum += val.getSum(noRed)
        return totSum

    def __repr__(self):
        retStr="["
        for val in self.vals:
            retStr+=str(val)+","
        return retStr+"]"

class DictNode:
    def __init__(self):
        self.vals=[]
        self.parent=None

    def getSum(self,noRed=False):
        if noRed:
            if "red" in self.vals:
                return 0
        totSum=0
        for val in self.vals:
            if type(val)==int:
                totSum+=val
            elif type(val)==DictNode or type(val)==ListNode:
                totSum+=val.getSum(noRed)
        return totSum

    def __repr__(self):
        retStr="{"
        for val in self.vals:
            retStr+=str(val)+","
        return retStr+"}"

line=f.readline().rstrip()

#line='{"d":"red","e":[1,2,3,4],"f":5}'
curNode=None
i=0
print(len(line))
while i<len(line):
    if line[i]=="[":
        if curNode==None:
            curNode=ListNode()
            root=curNode
        else:
            curNode.vals.append(ListNode())
            curNode.vals[-1].parent=curNode
            curNode=curNode.vals[-1]
        i+=1
    elif line[i]=="{":
        if curNode==None:
            curNode=DictNode()
            root=curNode
        else:
            curNode.vals.append(DictNode())
            curNode.vals[-1].parent=curNode
            curNode=curNode.vals[-1]
        while line[i]!=":":
            i+=1
        i+=1
    elif line[i]=="]" or line[i]=="}":
        curNode=curNode.parent
        i+=1
    elif line[i].isdigit() or line[i]=="-":
        curString = ""
        while line[i].isdigit() or line[i] == "-":
            curString += line[i]
            i += 1
        curNode.vals.append(int(curString))
    elif line[i]=='"':
        i+=1
        curString=""
        while line[i]!='"':
            curString+=line[i]
            i+=1
        i+=1
        curNode.vals.append(curString)
    elif line[i]==",":
        if type(curNode)==DictNode:
            while line[i]!=":":
                i+=1
            i+=1
        else:
            i+=1
    #print(i)
print(root.getSum()) # part 1
print(root.getSum(noRed=True)) # part 2