import sys; input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
q = deque()
visited = [ [ False ] * m for _ in range(n) ]
ans = 0

dy = [0,0,-1,1]
dx = [-1,1,0,0]

graph = [[] for _ in range(n)]
for i in range(n):
    line = list(input().strip())
    for j in range(len(line)):
        if line[j] == 'I':
           q.append((i,j))
           visited[i][j] = True
        graph[i].append(line[j])
        
while q:
    y,x = q.popleft()

    for i in range(4):
        ny = y + dy[i]; nx = x + dx[i]
        
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and graph[ny][nx]!='X':
            if graph[ny][nx] == 'P': ans+=1
            visited[ny][nx] = True
            q.append((ny,nx))

print(ans) if ans else print("TT")