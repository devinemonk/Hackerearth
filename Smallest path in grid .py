from collections import deque
 
 
def is_valid_move(x, y, row, col):
    return x>=0 and x<row and y>=0 and y<col
 
 
def trav(g, dist, si, sj, n, m):
    q = deque([(si, sj)])
    dist[si][sj] = 0
    # curr_dist = 1
    while q:
        x, y = q.popleft()
        if is_valid_move(x-1, y, n, m) and g[x-1][y] and dist[x-1][y] == -1:
            dist[x-1][y] = dist[x][y] + 1
            q.append((x-1, y))
        if is_valid_move(x+1, y, n, m) and g[x+1][y] and dist[x+1][y] == -1:
            dist[x+1][y] = dist[x][y] + 1
            q.append((x+1, y))
        if is_valid_move(x, y-1, n, m) and g[x][y-1] and dist[x][y-1] == -1:
            dist[x][y-1] = dist[x][y] + 1
            q.append((x, y-1))
        if is_valid_move(x, y+1, n, m) and g[x][y+1] and dist[x][y+1] == -1:
            dist[x][y+1] = dist[x][y] + 1
            q.append((x, y+1))
        # curr_dist += 1
 
 
def solve():
    n, m, q = [int(i) for i in input().split()]
    g = []
    dist = [[-1]*m for _ in range(n)]
    for _ in range(n):
        g.append([0 if c=='*' else 1 for c in input()])
    si, sj = [int(i) for i in input().split()]
    trav(g, dist, si-1, sj-1, n, m)
    # print dist
    for _ in range(q):
        query = [int(i) for i in input().split()]
        print (dist[query[0]-1][query[1]-1])
try:
    solve()
except:
    pass
