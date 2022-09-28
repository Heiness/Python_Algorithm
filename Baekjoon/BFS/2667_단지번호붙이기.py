import sys
from collections import deque
input = sys.stdin.readline

cnt = 0
answer = []
n = int(input())
graph = [ list(map(int,input().strip())) for _ in range(n)]

def bfs(y, x):
    
    global cnt
    q = deque()
    q.append((y,x))
    graph[y][x]=0
    total = 1
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=ny<n and 0<=nx<n and graph[ny][nx]==1:
                q.append((ny,nx))
                graph[ny][nx]=0
                total+=1
    
    cnt+=1
    answer.append(total)
                

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            bfs(i,j)

print(cnt)
for c in sorted(answer):
    print(c)
