# cook your dish here
x,y=map(int,input().split())
if abs(x-y)<=2:
    print("Interesting")
else:
    print("Boring")