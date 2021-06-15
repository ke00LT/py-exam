a=int(input())
b=int(input())
sum=(a*2+b)%3
if sum==0:
    print("普通")
elif sum==1:
    print("吉")
else:
    print("大吉") 