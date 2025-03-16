import sys; input = sys.stdin.readline
from collections import deque

K = int(input())

def dfs(graph, V):
    for i in range(1,V+1):
        if not visited[i] : visited[i] = 1
        q = deque()
        q.append(i)

        while q:
            now = q.popleft()

            for j in graph[now]:
                if not visited[j]: 
                    visited[j] = -visited[now]
                    q.append(j)
                else:
                    if visited[now] == visited[j]: return False
    return True


for _ in range(K):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    if dfs(graph, V): print("YES")
    else: print("NO")