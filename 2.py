a=int(input(""))
if a<120:
    print("Summer months:%.2fNon-Summer months:%.2f"%(a*2.10,a*2.10))
elif a<330:
    print("Summer months:%.2fNon-Summer months:%.2f"%(120*2.10+(a-120)*3.02,120*2.10+(a-120)*2.68))
elif a<500:
    print("Summer months:%.2fNon-Summer months:%.2f"%(120*2.10+(330-120)*3.02+(a-330)*4.39,120*2.10+(330-120)*2.68+(a-330)*3.61))
elif a<700:
    print("Summer months:%.2fNon-Summer months:%.2f"%(120*2.10+(330-120)*3.02+(500-330)*4.39+(a-500)*4.97,120*2.10+(330-120)*2.68+(500-330)*3.61+(a-500)*4.01))
else:
    print("Summer months:%.2fNon-Summer months:%.2f"%(120*2.10+(330-120)*3.02+(500-330)*4.39+(700-500)*4.97+(a-700)*5.63,120*2.10+(330-120)*2.68+(500-330)*3.61+(700-500)*4.01+(a-700)*4.50))