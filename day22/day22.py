import queue as q
import math as mt

pHp=50
pMp=500
bHp=55
bDmg=8

moveQ=q.Queue()
# the queue stores gamestates, where the last four numbers are the effects, mana spent, and whose turn it is
moveQ.put((pHp,pMp,bHp,0,0,0,0,0))
part = 1

def handleEffects(pmp,bhp,shield,poison,regen):
    if shield>0:
        shield-=1
        armor=7
    else:
        armor=0
    if poison>0:
        poison-=1
        bhp-=3
    if regen>0:
        regen-=1
        pmp+=101
    return (pmp,bhp,armor,shield,poison,regen)

def bossTurn(php,pmp,bhp,shield,poison,regen,spent):
    global minMana
    pmp,bhp,armor,shield,poison,regen=handleEffects(pmp,bhp,shield,poison,regen)
    if bhp<=0:
        if spent<minMana:
            minMana=spent
        return
    if php<=0:
        return
    php=php-max(1,bDmg-armor)
    moveQ.put((php,pmp,bhp,shield,poison,regen,spent,0))

def playerTurn(php,pmp,bhp,shield,poison,regen,spent):
    global minMana
    if part==2:
        php-=1
        if php<=0:
            return
    pmp,bhp,armor,shield,poison,regen=handleEffects(pmp,bhp,shield,poison,regen)
    if bhp<=0:
        if spent<minMana:
            minMana=spent
        return
    if php<=0:
        return
    if pmp >= 53:  # magic missile, deal 4 dmg for 53 mana
        magicMissile(bhp, php, pmp, poison, regen, shield, spent)
    if pmp >= 73:  # drain, deal 2 dmg heal 2 for 73 mana
        drain(bhp, php, pmp, poison, regen, shield, spent)
    if pmp >= 113 and shield == 0:  # shield, costs 113, lasts 6 turns, sets armor to 7
        makeShield(bhp, php, pmp, poison, regen, spent)
    if pmp >= 173 and poison <= 0:  # costs 173, lasts 6 turns, 3 dmg per turn
        castPoison(bhp, php, pmp, regen, shield, spent)
    if pmp >= 229 and regen <= 0:  # recharge, costs 229, regen 101 mana for 5 turns
        regenerate(bhp, php, pmp, poison, shield, spent)


def regenerate(bhp, php, pmp, poison, shield, spent):
    regen = 5
    pmp -= 229
    moveQ.put((php, pmp, bhp, shield, poison, regen, spent + 229, 1))


def castPoison(bhp, php, pmp, regen, shield, spent):
    pmp -= 173
    poison = 6
    moveQ.put((php, pmp, bhp, shield, poison, regen, spent + 173, 1))


def makeShield(bhp, php, pmp, poison, regen, spent):
    pmp -= 113
    shield = 6
    moveQ.put((php, pmp, bhp, shield, poison, regen, spent + 113, 1))


def drain(bhp, php, pmp, poison, regen, shield, spent):
    pmp -= 73
    bhp -= 2
    php += 2
    moveQ.put((php, pmp, bhp, shield, poison, regen, spent + 73, 1))


def magicMissile(bhp, php, pmp, poison, regen, shield, spent):
    pmp -= 53
    bhp -= 4
    moveQ.put((php, pmp, bhp, shield, poison, regen, spent + 53, 1))


minMana=mt.inf
while not moveQ.empty():
    move=moveQ.get()
    #print(move)
    php,pmp,bhp,shield,poison,regen,spent,turn=move
    if spent<1000:
        if turn==0:
            playerTurn(php,pmp,bhp,shield,poison,regen,spent)
        else:
            bossTurn(php,pmp,bhp,shield,poison,regen,spent)

print(minMana)

part=2

moveQ.put((pHp,pMp,bHp,0,0,0,0,0))

minMana=mt.inf
while not moveQ.empty():
    move=moveQ.get()
    php,pmp,bhp,shield,poison,regen,spent,turn=move
    if spent<1350:
        if turn==0:
            playerTurn(php,pmp,bhp,shield,poison,regen,spent)
        else:
            bossTurn(php,pmp,bhp,shield,poison,regen,spent)
print(minMana)