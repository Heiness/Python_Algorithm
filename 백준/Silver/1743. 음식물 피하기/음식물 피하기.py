import sys; input = sys.stdin.readline
from collections import deque

n,m,k = map(int,input().split())
graph = [ [0] * m for _ in range(n) ]
for _ in range(k):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1

dy = [0,0,-1,1]
dx = [-1,1,0,0]
visited = [[0] * m for _ in range(n)]

def bfs(y, x):
    res = 1 
    q = deque()
    q.append((y,x))
    visited[y][x] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=ny<n and 0<=nx<m and graph[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny,nx))
                res+=1
    
    return res

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            ans=max(ans,bfs(i,j))
print(ans)