NUM=29000000/10 # the div by 10 is to simplify the problem, as all elves deliver in multiples of ten

house=2*int(NUM**.5) # the number of presents for a house is lower bounded by the sum of all integers less than it
# this means that presents>=house(house+1)/2, which lets us set a lower bound on the house
while True:
    presents=house+1
    for i in range(2,int(house**.5)):
        if house%i==0:
            presents+=i+house/i
    if presents>NUM:
        print(house,presents) # part 1
        break
    house+=1

NUM2=NUM/1.1 # as all elves deliver in multiples of 11, this simplifies things slightly

house=2*int(NUM2**.5)
while True:
    presents=0
    for j in range(1,51):
        if house%j==0:
            presents+=house/j
    if presents>NUM2:
        print(house,presents) # part 2
        break
    house+=1