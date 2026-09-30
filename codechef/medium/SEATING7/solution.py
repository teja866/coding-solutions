# cook your dish here
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    a=[0]*(n+1)
    for i in range(m):
        seat=int(input())
        a[seat]=seat 
    missing=[]
    for i in range(n+1):
        if a[i]==0:
            missing.append(i)
    print(missing)