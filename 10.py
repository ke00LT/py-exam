n,m=input("輸入Ｎ及Ｍ為：").split()
b=[]
c=[]
for i in range(int(n)):
    a=input('輸入矩陣數值第%d列為:'%(i+1)).split()
    b.append(a)
for i in range(int(m)):
    print('輸出矩陣數值第%d列為:'%(i+1),end="")
    for j in range(int(n)):
        print(b[j][i],end=" ")
    print()