n=int(input())
a=list(map(int,input().split()))
ans=0
mnr=n
mxl=-1
for i in range(n):
    ans+=abs(a[i]-i-1)
    l=i+1
    r=a[i]
    if l>r:
        l,r=r,l
    mnr=min(mnr,r)
    mxl=max(mxl,l)
if mxl>mnr:
    ans+=2*(mxl-mnr)
print(ans)
