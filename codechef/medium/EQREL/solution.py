# cook your dish here
n=int(input().strip())
a=list(map(int,input().split()))
minH=min(a)
total=sum(a)-n*minH
print(total)
