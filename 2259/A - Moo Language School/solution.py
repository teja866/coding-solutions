t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input().strip()
    ans=0
    for i in range(0,n,k):
        has_free=False
        for j in range(i,i+k):
            if s[j]=='0':
                has_free=True
                break
        if not has_free:
            ans+=1
    print(ans)