import sys; input = sys.stdin.readline
import heapq

def dijkA(a):
    pq = []
    heapq.heappush(pq,(0,a))
    dist = [sys.maxsize] * (N+1)
    while pq:
        nowW, nowV = heapq.heappop(pq)
        if(dist[nowV]<nowW): continue

        for nextV, nextW in graph[nowV]:
            d = nextW + nowW
            if(dist[nextV]>d):
                dist[nextV] = d
                heapq.heappush(pq,(d, nextV))
    return dist

def dijkB(a):
    pq = []
    heapq.heappush(pq,(0,a,0))
    dist = [[sys.maxsize] * (N+1) for _ in range(2) ]
    while pq:
        nowW, nowV, C = heapq.heappop(pq)
        if(dist[C][nowV]<nowW): continue

        for nextV, nextW in graph[nowV]:
            d = nowW + (nextW/2 if C==0 else nextW*2)
            if(dist[1 if C==0 else 0][nextV]>d):
                dist[1 if C==0 else 0][nextV] = d    
                heapq.heappush(pq,(d, nextV, 1 if C==0 else 0))
    return dist

ans = 0
N, M = map(int, input().split())
graph = [ []  for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dist1 = dijkA(1)
dist2 = dijkB(1)

for i in range(2,N+1):
    ans+= 1 if dist1[i] < dist2[0][i] and dist1[i] < dist2[1][i] else 0
print(ans)