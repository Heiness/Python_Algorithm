import sys; input = sys.stdin.readline
import heapq

N, M, R = map(int,input().split())
items = list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
tmp = []

for _ in range(R):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijk(start):
    global M
    distance = [sys.maxsize] * (N+1)
    pq = []
    heapq.heappush(pq,(0,start))
    distance[start] = 0

    while pq:
        c, now = heapq.heappop(pq)

        if c > distance[now]: continue

        for next, w in graph[now]:
            nc = c + w
            if distance[next] > nc:
                distance[next] = nc
                heapq.heappush(pq,(nc,next))

    t = 0
    for i in range(1,N+1):
        if M >= distance[i]: t+=items[i-1]
    tmp.append(t)

for i in range(1,N+1):
    dijk(i)

print(max(tmp))