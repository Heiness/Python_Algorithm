import sys; input = sys.stdin.readline
import heapq
INF = sys.maxsize

v, e = map(int,input().split())
graph = [[] for _ in range(v+1) ]
dist = [INF]*(v+1)

start = int(input())

for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    # graph[b].append((a,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0
    
    while q:
        d, now = heapq.heappop(q)
        
        if dist[now] < d:
            continue
        
        for v,w in graph[now]:
            cost = d + w
            if cost < dist[v]:
                heapq.heappush(q,(cost,v))
                dist[v]=cost
                
dijkstra(start)
        
for i in range(1,v+1):
    if dist[i]==INF: print("INF")
    else: print(dist[i])
    
