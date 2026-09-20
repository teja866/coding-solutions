# cook your dish here
n,k=map(int,input().split())
total=(n//2)+1
if k<=total:
    print(total-k)
else:
    print(0)