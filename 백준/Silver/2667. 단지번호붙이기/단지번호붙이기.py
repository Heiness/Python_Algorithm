import sys; input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [ list(map(int,input().strip())) for _ in range(N) ]

dy = [0,0,-1,1]
dx = [-1,1,0,0]
visited = [ [False] * N for _ in range(N) ]
ans = 0
countList = []

def bfs(y,x):
    cnt = 1
    q = deque()
    q.append((y,x))
    visited[y][x]=True

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<N and 0<=nx<N and graph[ny][nx]==1 and not visited[ny][nx]:
                cnt+=1
                visited[ny][nx] = True
                q.append((ny,nx))
    
    countList.append(cnt)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i,j)
            ans+=1

print(ans)
for v in sorted(countList):
    print(v)