a=int(input('輸入第一行正整數為:'))
b=(input('第二行數列中的數字為:').split())
c=[]
if a==len(set(b)):
    print('沒重複')
else:
    for i in b:
        c.append(b.count(i))
print(b[c.index(max(c))])  
print(max(c))