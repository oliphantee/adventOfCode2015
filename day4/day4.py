import hashlib

f=open('day4.txt',"r")

code=f.readline().rstrip()
num=0
while True:
    hashed=hashlib.md5((code+str(num)).encode())
    if str(hashed.hexdigest())[0:6]=="000000":
        break
    num+=1
print(num)

f.close()