# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cnt=0
    for i in range(n):
        if a[i]>=1000:
            cnt+=1
    print(cnt)