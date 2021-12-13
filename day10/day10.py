val="1321131112"
T_MAX=50

def lookAndSay(val):
    output=""
    curCount=1
    prev=val[0]
    for c in val[1:]:
        if c==prev:
            curCount+=1
        else:
            output+=str(curCount)+prev
            prev=c
            curCount=1
    output+=str(curCount)+prev
    return output

for i in range(T_MAX):
    val=lookAndSay(val)

print(len(val))