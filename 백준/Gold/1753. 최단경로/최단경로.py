import sys; input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))

dist = [sys.maxsize] * (N+1)
def dijk(start):
    pq = []

    dist[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        cost, now = heapq.heappop(pq)

        if cost > dist[now]: continue
        
        for weight, next in graph[now]:
            nc = cost + weight

            if nc < dist[next]:
                dist[next] = nc
                heapq.heappush(pq,(nc,next))

dijk(start)
for i in range(1, N+1):
    if dist[i]==sys.maxsize:
        print("INF")
    else:
        print(dist[i])