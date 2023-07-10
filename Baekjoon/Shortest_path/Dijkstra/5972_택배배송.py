import sys; input = sys.stdin.readline
import heapq
INF = sys.maxsize

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0
    
    while q:
        d, now = heapq.heappop(q)
        
        if dist[now] < d:
            continue
        
        for v, w in graph[now]:
            cost = d + w
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q, (cost, v))
                
dijkstra(1)
print(dist[n])
