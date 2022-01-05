import queue as q
import math as mt

pHp=50
pMp=500
bHp=55
bDmg=8

moveQ=q.Queue()
# the queue stores gamestates, where the last four numbers are the effects and mana spent
moveQ.put((pHp,pMp,bHp,0,0,0,0))

minMana=mt.inf
while not moveQ.empty():
    move=moveQ.get()
    php,pmp,bhp,shield,poison,regen,spent=move
    if poison>0:
        bhp-=3
    if shield>0:
        armor=7
    if regen>0:
        pmp+=101
    else:
        armor=0
    if bhp<=0:
        print(move)
        if spent<minMana:
            minMana=spent
    elif php<0:
        pass
    elif spent>1000: # to prevent infinite recursion
        pass
    else:
        if pmp>=53:
            moveQ.put((php-max(1,bDmg-armor),pmp-53,bhp-4,shield-1,poison-1,regen-1,spent+53))
        if pmp>=73:
            moveQ.put((php-max(1,bDmg-armor)+2,pmp-73,bhp-2,shield-1,poison-1,regen-1,spent+73))
        if pmp>=113 and shield<=0:
            moveQ.put((php-1,pmp-113,bhp,6,poison-1,regen-1,spent+113))
        if pmp>=173 and poison<=0:
            moveQ.put((php-max(1,bDmg-armor),pmp-173,bhp,shield-1,6,regen-1,spent+173))
        if pmp>=229 and regen<=0:
            moveQ.put((php-max(1,bDmg-armor),pmp-229,bhp,shield-1,poison-1,5,spent+229))

print(minMana)