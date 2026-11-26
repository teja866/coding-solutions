# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    l=max(x-y,x-z)
    r=min(x+y,x+z)
    print(r-l)
    