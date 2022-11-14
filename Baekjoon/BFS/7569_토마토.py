import sys; input = sys.stdin.readline
from collections import deque

m, n, h = map(int,input().split())
graph = [ list(list(map(int,input().split())) for j in range(n)) for i in range(h) ]

dz = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dx = [0,0,0,0,1,-1]

def bfs():    
    
    while q:
        z,y,x,cnt = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and graph[nz][ny][nx]==0:
                q.append((nz,ny,nx,cnt+1))
                graph[nz][ny][nx]=1    
    
    for i in graph:
        for j in i:
            if 0 in j:
                return -1
            
    return cnt

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1:
                q.append((i,j,k,0))
            
print(bfs())
