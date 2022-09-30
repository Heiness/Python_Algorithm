from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [ list(map(int,input().strip())) for _ in range(n) ]
visited = [ [0] * m for _ in range(n) ] # 0: 미방문, 1: 방문

def bfs(y, x):
    global n,m
    q = deque()
    q.append((y,x))

    visited[y][x] = 1

    dy = [0,0,1,-1]
    dx = [1,-1,0,0]

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and graph[ny][nx]==1:
                visited[ny][nx]=visited[y][x]+1
                q.append((ny,nx))


bfs(0,0)
print(visited[-1][-1])
