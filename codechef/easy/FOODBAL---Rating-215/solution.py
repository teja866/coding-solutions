# cook your dish here
f1,p1,f2,p2=map(int,input().split())
dish1=abs(f1-p1)
dish2=abs(f2-p2)
if dish1<dish2:
    print("First")
elif dish1==dish2:
    print("Both")
else:
    print("Second")