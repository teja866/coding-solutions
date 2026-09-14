# cook your dish here
n=int(input())
a=list(map(int,input().split()))

mid=(a[0]+a[-1])//2

if n%2==0:
    if a[n//2]<=mid:
        print(a[n//2])
else:
    print(mid)
    
        