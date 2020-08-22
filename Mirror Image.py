
class Node():
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right= None

def find(f,r,n):
    if f==None or r==None:
        return -1
    if f.data==n:
        return r.data
    if r.data==n:
        return f.data
    
    c=find(f.left,r.right,n)
    if c!=-1:
        return c
    return find(f.right,r.left,n)


x,y=map(int,input().split())
a=[Node(i) for i in range(x+1)]
root=a[1]
for i in range(x-1):
    n,m,o=map(str,input().split())
    n=a[int(n)]
    m=a[int(m)]
    if o=='L':
        n.left=m
    else:
        n.right=m


for i in range(y):

    q=int(input())
    if q==1:
        print(1)
    else:
        c=find(root.left,root.right,q)
        print(c)
