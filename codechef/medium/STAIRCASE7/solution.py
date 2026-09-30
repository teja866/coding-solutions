# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range(1,n):
        if (a[i]-a[i-1])!=1:
            count+=1 
    print(count)