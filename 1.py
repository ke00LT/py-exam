def h(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
alist=[]
a=input("請輸入正整數:")
for i in range(len(a),1,-1):
    for j in range(i):
        b=a[j:i]
        b=int(b)
        if h(b)==True:
            alist.append(b)
if alist !=[]:
    print("子字串中最大的質數為:%d"%(max(alist)))
else:
    print("子字串中最大的質數為: No prime found")