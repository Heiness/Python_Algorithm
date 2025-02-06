import sys; input = sys.stdin.readline
from collections import deque

dy = [0,0,-1,1]
dx = [-1,1,0,0]

M, N, K = map(int,input().split())
graph = [ [0] * N for _ in range(M) ]
for _ in range(K):
    a, b, c, d = map(int,input().split())

    for i in range(b,d):
        for j in range(a,c):
            graph[i][j] = 1

ans=[]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    cnt = 1
    graph[y][x] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<M and 0<=nx<N and not graph[ny][nx]:
                q.append((ny,nx))
                graph[ny][nx] = 1
                cnt+=1
    
    ans.append(cnt)


for i in range(M):
    for j in range(N):
        if not graph[i][j]: bfs(i,j)

print(len(ans))
print(*sorted(ans))