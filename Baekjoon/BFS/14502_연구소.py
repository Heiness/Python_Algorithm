import sys; input = sys.stdin.readline
from collections import deque
from copy import deepcopy

n, m = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(n) ]
result = 0

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def make_wall(cnt):
    if cnt==3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                make_wall(cnt+1)
                graph[i][j]=0
            
def bfs():
    q = deque()
    copy_map = deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if copy_map[i][j]==2:
                q.append((i,j))
    
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<m and copy_map[ny][nx]==0:
                q.append((ny,nx))
                copy_map[ny][nx]=2
    
    global result
    t = 0

    for i in range(n):
        for j in range(m):
            if copy_map[i][j]==0:
                t+=1
    
    result = max(result,t)


make_wall(0)
print(result)