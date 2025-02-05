import sys; input = sys.stdin.readline
from collections import deque
from itertools import combinations
from copy import deepcopy

N,M = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N) ]
cnt = 0
ans = 0
dy = [0,0,-1,1]
dx = [-1,1,0,0]

virus_coor = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus_coor.append((i,j))

def bfs(graph):
    q = deque(virus_coor)
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=ny<N and 0<=nx<M and not graph[ny][nx]:
                graph[ny][nx] = 2
                q.append((ny,nx))

def cntVirus(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt+=1
    return cnt

def dfs(cnt):
    global ans

    if cnt == 3:
        copyGraph = deepcopy(graph)
        bfs(copyGraph)
        ans = max(ans, cntVirus(copyGraph))
        return 

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(cnt+1)
                graph[i][j] = 0

dfs(0)
print(ans)