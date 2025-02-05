import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
graph = [ list(map(int,input().strip())) for _ in range(N) ]
visited = [[[0,0] for _ in range(M)] for i in range(N)]
visited[0][0][0] = 1

dy = [0,0,-1,1]
dx = [-1,1,0,0]

q = deque()
q.append((0,0,0))

while q:
    y, x, c = q.popleft()
    
    if y == N-1 and x == M-1:
        print(visited[y][x][c])
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny<0 or N<=ny or nx<0 or M<=nx:
            continue

        if graph[ny][nx]==1 and not c:
            visited[ny][nx][1] = visited[y][x][0] + 1
            q.append((ny,nx,1))
        
        elif graph[ny][nx]==0 and visited[ny][nx][c] == 0:
            visited[ny][nx][c] = visited[y][x][c] + 1
            q.append((ny,nx,c))

else:
    print(-1)