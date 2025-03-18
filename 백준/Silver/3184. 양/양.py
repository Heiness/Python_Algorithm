import sys; input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
graph = [ list(input().strip()) for _ in range(r) ]
visited = [[0] * c for _ in range(r)]
dy = [0,0,-1,1]
dx = [-1,1,0,0]
ans = [0,0]

def bfs(y, x):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    tmp = [0,0]

    if graph[y][x] == 'v': tmp[1]+=1
    elif graph[y][x] =='o': tmp[0]+=1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<r and 0<=nx<c and not visited[ny][nx] and graph[ny][nx]!='#':
                visited[ny][nx] = 1
                q.append((ny,nx))

                if graph[ny][nx] == 'v': tmp[1]+=1
                elif graph[ny][nx] =='o': tmp[0]+=1
    
    if tmp[1]>=tmp[0]: ans[1]+=tmp[1]
    else: ans[0]+=tmp[0]

for i in range(r):
    for j in range(c):
        if graph[i][j]!='#' and not visited[i][j]:
            bfs(i,j)

print(*ans)