# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    min1=min(a)
    sum1=0
    for i in range(n):
        if a[i]==min1:
            continue
        else:
            sum1+=a[i]
    print(sum1)