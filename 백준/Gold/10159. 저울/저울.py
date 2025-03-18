import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
visited = [ [0]*(n+1) for _ in range(n+1) ]
graph = [[] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def dfs(a, b):
    for i in graph[b]:
        if not visited[a][i]:
            visited[a][i] = 1
            visited[i][a] = 1
            dfs(a, i)


for i in range(1,n+1):
    visited[i][i]=1
    dfs(i,i)

for i in visited[1:]:
    print(n-sum(i[1:]))