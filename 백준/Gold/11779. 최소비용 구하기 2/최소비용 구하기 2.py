import sys; input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append([b,c])

start, end = map(int, input().split())

pq = []
visited = [sys.maxsize] * (N+1)
path = [[] for _ in range(N+1)]
heapq.heappush(pq,[0,start])
path[start].append(start)
visited[start] = 0

while pq:
    cost, now = heapq.heappop(pq)

    if cost > visited[now]: continue
    if now == end: break

    for next, nc in graph[now]:
        tmp = cost + nc

        if visited[next] > tmp:
            visited[next] = tmp
            path[next] = []
            for i in path[now]:
                path[next].append(i)
            path[next].append(next)
            heapq.heappush(pq,[tmp,next])

print(visited[end]) 
print(len(path[end]))
print(*path[end])