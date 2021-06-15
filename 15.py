a=input("輸入一組四位數字為:")
al=list(a)
bl=[]
for i in al:
    i=int(i)
    i=(i+7)%10
    bl.append(i)
print("輸出加密後的數字為:%d%d%d%d"%(bl[2],bl[3],bl[0],bl[1]))