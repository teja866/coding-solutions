# cook your dish here
s=input().strip()
n=len(s)
count=0
for i in range(n):
    if i==2 and s[i]=='n' or i==3 and s[i]=='t' or i==4 and s[i]=='a':
        count=1
    else:
        count=0
if count>0:
    print("Yes")
else:
    print("No")