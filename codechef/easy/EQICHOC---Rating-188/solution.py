# cook your dish here
r,l=map(int,input().split())
total=r-l
if total<0:
    print(total+10)
else:
    print(total)