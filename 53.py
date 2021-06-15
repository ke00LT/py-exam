import math
a=float(input("請輸入路程公里數(km):"))
if a//1.5<1:
    print("所需車資為:75")
else:
    print("所需車資為:",math.ceil((a-1.5)/0.25)*5+75)
