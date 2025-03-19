import sys; input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [ list(map(int,input().strip())) for _ in range(n) ]

visited=[ [0] * m for _ in range(n) ]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def bfs(y,x):
    visited[y][x] = 1
    q = deque()
    q.append((y,x))

    while q:
        y, x = q.popleft()

        if y==n-1:
            return True
        
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=ny<n and 0<=nx<m and graph[ny][nx]==0 and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny,nx))
    
    return False


for j in range(m):
    if not visited[0][j] and graph[0][j]==0:
        if bfs(0,j):
            print("YES")
            break
else: print("NO")