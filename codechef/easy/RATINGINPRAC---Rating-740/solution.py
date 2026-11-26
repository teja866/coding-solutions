t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    flag=True
    for i in range(n-1):
        if d[i]>d[i+1]:
            flag=False
            break
    print("Yes" if flag else "No")
    t -= 1
