import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [ [] for _ in range(N) ]
visited = [False] * N
ans = False

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n, depth):
    global ans
    visited[n] = True

    if depth==5:
        print(1)
        ans = True
        return True

    for i in graph[n]:
        if not visited[i]:
            if dfs(i,depth+1): return True
            visited[i] = False
    visited[n] = False

for i in range(N):
    dfs(i,1)
    if ans: break
else: print(0)