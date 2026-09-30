# cook your dish here
b,h,c=map(int,input().split())
maxbread=b//2
total=h+c 
if maxbread>total:
    print(maxbread)
else:
    print(total)