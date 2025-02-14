import sys; input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [sys.maxsize] * (N+1)

for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((b,c))

start, end = map(int,input().split())

def dijk(n: int):
    global end
    pq = []
    heapq.heappush(pq,(0, n))
    distance[n] = 0

    while pq:
        c, now = heapq.heappop(pq)

        if distance[now]<c: continue
        if now == end: return

        for next, cost in graph[now]:
            if distance[next] > c + cost:
                distance[next] = c + cost
                heapq.heappush(pq,(c + cost,next))

dijk(start)
print(distance[end])