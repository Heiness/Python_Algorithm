import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [ list(map(int,input().strip())) for _ in range(N) ]
visited = [ [[0] * 2 for _ in range(M)] for __ in range(N) ]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

q = deque()
q.append((0,0,0))
visited[0][0][0] = 1

while q:
    y, x, c = q.popleft()

    if y==N-1 and x==M-1:
        print(visited[y][x][c])
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<N and 0<=nx<M:
            # 벽이 있지만 안부셨을때
            if arr[ny][nx] == 1 and not c and not visited[ny][nx][1]:
                visited[ny][nx][1] = visited[y][x][c] + 1
                q.append((ny,nx,c+1))

            # 벽이 없을 때
            elif arr[ny][nx] == 0 and not visited[ny][nx][c]:
                visited[ny][nx][c] = visited[y][x][c] + 1
                q.append((ny,nx,c))

else: print(-1)