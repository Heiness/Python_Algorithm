import sys; input = sys.stdin.readline
from collections import deque

dy = [-1,-2,-2,-1,1,2,2,1]
dx = [-2,-1,1,2,-2,-1,1,2]

for _ in range(int(input())):
    l = int(input())
    graph = [ [0] * l for _ in range(l) ]
    q = deque()

    a, b = map(int,input().split())
    q.append((a,b,0))
    graph[a][b] = 1 # 1 체스
    a, b = map(int,input().split())
    graph[a][b] = 2 # 2 도착지

    while q:
        y, x, c = q.popleft()

        if graph[y][x] == 2:
            print(c)
            break

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<l and 0<=nx<l and graph[ny][nx]!=1:
                if graph[ny][nx]==0: graph[ny][nx] = 1
                q.append((ny,nx,c+1))