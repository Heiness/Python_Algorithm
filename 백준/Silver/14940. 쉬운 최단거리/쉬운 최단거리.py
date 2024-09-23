import sys; input = sys.stdin.readline
from collections import deque
from pprint import pprint

n,m = map(int,input().split())
graph = [ [] for _ in range(n) ]
dist = [[0] * m for _ in range(n)]
dy = [0,0,-1,1]
dx = [-1,1,0,0]
q = deque()

for i in range(n):
    line = list(map(int,input().split()))
    for j in range(len(line)):
        if line[j]==2: 
            q.append([i,j])
        graph[i].append(line[j])

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]; nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m and graph[ny][nx]==1 and not dist[ny][nx]:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny,nx))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: dist[i][j]=0
        elif graph[i][j] == 1 and dist[i][j] == 0: dist[i][j] = -1

for i in dist:
    print(*i)