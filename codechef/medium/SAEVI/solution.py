# cook your dish here
n,k=map(int,input().split())
a=list(map(int,input().split()))
sum1=0
for i in range(0,n,2):
    if a[i]>=2*k:
        sum1+=a[i]
print(sum1)
        
    