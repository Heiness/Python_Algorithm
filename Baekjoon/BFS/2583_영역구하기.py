import sys; input = sys.stdin.readline
from pprint import pprint
from collections import deque

n, m, k = map(int,input().split())
graph = [ [0] * m for _ in range(n) ]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

for _ in range(k):
    x, y, nx, ny = map(int,input().split())
    for i in range(y,ny):
        for j in range(x,nx):
            graph[i][j]=1

def bfs(y,x):
    area = 1
    q = deque()
    q.append((y,x))
    graph[y][x]=1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<m and graph[ny][nx]==0:
                graph[ny][nx]=1
                q.append((ny,nx))
                area+=1
    
    return area

area_list = []
cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            area_list.append(bfs(i,j))
            cnt+=1

print(cnt)
print(*sorted(area_list))
