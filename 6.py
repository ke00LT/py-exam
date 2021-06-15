a=input('輸入值為:').split(",")
b=sorted(a)
c=sorted(a,reverse=True)
d=""
f=""
for i in b:
    d+=i
for i in c:
    f+=i
print(int(f)-int(d))    

