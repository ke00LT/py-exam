a,b=map(int,input("輸入月即日:").split(" "))
c=a*100+b
if c>120 and c<219:
    print("星座為:Aquarius")
elif c>218 and c<321:
    print("星座為:Pisces")
elif c>320 and c<421:
    print("星座為:Aries")
elif c>420 and c<522:
    print("星座為:Taurus")
elif c>521 and c<622:
    print("星座為:Gemini")
elif c>621 and c<723:
    print("星座為:Cancer")
elif c>722 and c<824:
    print("星座為:Leo")
elif c>823 and c<924:
    print("星座為: Virgo")
elif c>923 and c<1024:
    print("星座為:Libra")
elif c>1023 and c<1123:
    print("星座為:Scorpio")
elif c>1122 and c<1222:
    print("星座為:Sagittarius")
else:
    print("星座為:Capricorn")
