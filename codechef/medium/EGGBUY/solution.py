# cook your dish here
x,y,f=map(int,input().split())
near=12*x 
far=12*y+f 
print(near if near<far else far)