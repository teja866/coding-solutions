# cook your dish here
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    if a[i]>=10:
        count+=1
print(count)