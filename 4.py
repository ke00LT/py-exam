a=int(input("X軸座標:"))
b=int(input("Y軸座標:"))
if(a>0 and b>0):
    print("該點位於第一象限，離原點距離為根號%d"%(a**2+b**2))
elif(a<0 and b>0):
    print("該點位於第二象限，離原點距離為根號%d"%(a**2+b**2))
elif(a<0 and b<0):
    print("該點位於第三象限，離原點距離為根號%d"%(a**2+b**2))
elif(a>0 and b<0):
    print("該點位於第四象限，離原點距離為根號%d"%(a**2+b**2))
elif(a==0 and b==0):
    print("該點位於原點")
elif(a==0 and b>0):
    print("該點位於上半平面Y軸上，離原點距離為根號%d"%(a**2+b**2))
elif(a==0 and b>0):
    print("該點位於下半平面Y軸上，離原點距離為根號%d"%(a**2+b**2))
elif(a>0 and b==0):
    print("該點位於右半平面X軸上，離原點距離為根號%d"%(a**2+b**2))
elif(a<0 and b==0):
    print("該點位於左半平面X軸上，離原點距離為根號%d"%(a**2+b**2))             