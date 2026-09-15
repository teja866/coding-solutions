# cook your dish here
x=int(input())
count=0
for i in range(1,x+1):
    if i%6==0:
        count+=1
print(count)