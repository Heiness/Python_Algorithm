import sys; input = sys.stdin.readline
import heapq

M, N = map(int, input().split())
graph = [ list(map(int,input().strip())) for _ in range(N) ]

pq = []
heapq.heappush(pq,(graph[0][0],0,0))
dist = [[sys.maxsize] * M for _ in range(N)]
dist[0][0] = graph[0][0]
dy = [0,0,-1,1]
dx = [-1,1,0,0]


while pq:
    cost, y, x = heapq.heappop(pq)
    if cost > dist[y][x]: continue

    if y==N-1 and x==M-1: break
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<N and 0<=nx<M:
            nc = cost + graph[ny][nx]
            if dist[ny][nx]>nc:
                dist[ny][nx]=nc
                heapq.heappush(pq,(nc,ny,nx))

print(dist[N-1][M-1])