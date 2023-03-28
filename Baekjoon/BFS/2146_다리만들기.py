import sys; input = sys.stdin.readline
from collections import deque
from pprint import pprint

n = int(input())
graph = [ list(map(int,input().split())) for _ in range(n) ]
visited = [ [0]*n for _ in range(n) ]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def separate_island(y, x):
    global is_num
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    graph[y][x] = is_num

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<n and graph[ny][nx] and not visited[ny][nx]:
                graph[ny][nx] = is_num
                visited[ny][nx] = 1
                q.append((ny,nx))

def find_shortest_bridge(num):
    global ans
    q = deque()
    dist = [ [-1] * n for _ in range(n) ]

    for i in range(n): # 목표 섬 좌표 저장 및 dist 갱신
        for j in range(n):
            if graph[i][j] == num:
                q.append((i,j))
                dist[i][j] = 0
    
    while q: # 방문 여부 확인할 필요없다.
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0>ny or 0>nx or ny>=n or nx>=n:
                continue
            elif graph[ny][nx] and graph[ny][nx]!=num: # 새 섬 발견
                ans = min(ans, dist[y][x])
                return
            elif not graph[ny][nx] and dist[ny][nx]==-1: # 바다
                dist[ny][nx]=dist[y][x]+1
                q.append((ny,nx))

# 섬의 분리
is_num = 1
ans = sys.maxsize
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            separate_island(i,j)
            is_num+=1

# 최단 거리 계산
for i in range(1,is_num):
    find_shortest_bridge(i)

print(ans)
