import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
visited = [False] * (N+1)
ans = 0

def bfs(n):
    q = deque()
    q.append(n)

    visited[n] = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        ans+=1

print(ans)