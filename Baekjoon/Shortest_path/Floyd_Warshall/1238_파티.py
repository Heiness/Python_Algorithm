import sys; input = sys.stdin.readline
import heapq

INF = sys.maxsize
n, m, x = map(int,input().split())
result = [0] * (n+1)
graph = [[] for _ in range(n+1) ]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start, end):
    dist = [INF] * (n+1)
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
                heapq.heappush(q,(cost,v))
    
    if start==end:
        for i in range(1,n+1):
            result[i]+=dist[i]
    
    return dist[end]
    

for i in range(1,n+1): # 한명당 다익스트라
    result[i] += dijkstra(i,x)

print(max(result))
