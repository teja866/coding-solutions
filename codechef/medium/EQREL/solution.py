# cook your dish here
n=int(input())
a=list(map(int,input().split()))
count=0
if n==1:
    print(0)
else:
    for i in range(n):
        if a[i]!=min(a):
            a[i]-=1
            count+=1
    print(count)
        