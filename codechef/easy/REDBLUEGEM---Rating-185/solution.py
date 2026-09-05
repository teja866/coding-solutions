# cook your dish here
r,b,p,q=map(int,input().split())
a=r*p
c=b*q
print(a if a>c else c)