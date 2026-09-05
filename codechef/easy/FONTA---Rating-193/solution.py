# cook your dish here
s=input().strip()
n=len(s)
count=0
if n>=3 and s[n-3]=='n' and s[n-2]=='t' and s[n-1]=='a':
    print("Yes")
else:
    print("No")