import sys; input = sys.stdin.readline
from collections import deque

m, n = map(int,input().split())
graph = [ list(input().strip()) for _ in range(n) ]
visited = [ [ False ] * m for _ in range(n) ]
dy = [0,0,-1,1]
dx = [-1,1,0,0]

q = deque()

def bfs(y, x):
    global w,b
    color = graph[y][x]
    cnt = 1
    q.append((y,x))
    visited[y][x] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]; nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and color == graph[ny][nx]:
                cnt+=1
                q.append((ny,nx))
                visited[ny][nx] = True
    
    if color=="W": w+= cnt * cnt
    else: b+= cnt * cnt

w, b = 0, 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]: bfs(i,j)

print(w,b)