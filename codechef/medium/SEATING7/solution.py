# cook your dish here
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    occupied=list(map(int,input().split()))
    a=[0]*(n+1)
    for seat in occupied:
        a[seat]=seat 
    missing=[]
    for i in range(1,n):
        if a[i]==0:
            missing.append(i)
    result=missing[:k]
    print(*result)