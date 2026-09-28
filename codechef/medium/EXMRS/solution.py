# cook your dish here
c,m,w,p,r=map(int,input().split())
total=c*m-w*p 
print("Yes" if total>=r else "No")