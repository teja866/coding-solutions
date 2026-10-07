# cook your dish here
x,y,k=map(int,input().split())
flag=False
for i in range(1,x+1):
    if i*y==k:
        flag=True
print("Yes" if flag else "No")