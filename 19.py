a=int(input("組數為:"))
for i in range(a):
    b,c=map(int,input("第%d組為:"%(int(i)+1)).split())
    print("第%d組應收費用:%d"%(int(i)+1,b*250+c*175))