t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    flag=False
    for i in range(n-1):
        if d[i]<d[i+1]:
            flag=True
        else:
            flag=False
    print("Yes" if flag else "No")
    t -= 1
