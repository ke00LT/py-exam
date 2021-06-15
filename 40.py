a=int(input("搭了幾次電梯:"))
al=[1]
bl=[]
sum=0
for i in range(a):
    b=input()
    al.append(b)
for i in range(len(al)-1):
    bl.append(int(al[i+1])-int(al[i]))
for i in range(len(bl)):
    if int(bl[i])>0:
        sum+=(int(bl[i])*20)
    else:
        sum+=(int(bl[i])*-10)
print(sum,"元") 