# cook your dish here
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    a=[]
    for i in range(n):
        if i==m:
            val=int(input())
            a.append(val)
    print(a)