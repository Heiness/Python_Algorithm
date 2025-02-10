import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    for i in graph[n]:
        if not visited[i]:
            visited[i] = n
            dfs(i)

dfs(1)

for i in visited[2:]:
    print(i)