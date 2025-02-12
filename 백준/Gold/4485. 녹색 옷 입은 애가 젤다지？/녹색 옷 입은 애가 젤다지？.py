import sys; input = sys.stdin.readline
import heapq

tc = 0
while 1:
    N = int(input())
    tc+=1
    if not N: break

    graph = [ list(map(int,input().split())) for _ in range(N) ]
    distance = [[sys.maxsize] * N for _ in range(N)]

    pq = []
    heapq.heappush(pq,(graph[0][0],0,0))
    distance[0][0] = graph[0][0]
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    while pq:
        now_cost, y, x = heapq.heappop(pq)

        if now_cost > distance[y][x]: continue
        if y == N-1 and x == N-1: break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=ny<N and 0<=nx<N:
                next_cost = now_cost + graph[ny][nx]

                if next_cost < distance[ny][nx]:
                    distance[ny][nx] = next_cost
                    heapq.heappush(pq,(next_cost,ny,nx))

    print(f"Problem {tc}: {distance[N-1][N-1]}")