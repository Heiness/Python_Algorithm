import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

s = int(input())
f = list(map(int,input().split()))

ans = 0

def dfs(x):
    global ans
    visited[x] = 1

    if x in f: # 팬 만남
        return

    if not graph[x]:
        ans+=1
        return

    for next in graph[x]:
        if not visited[next]:
            dfs(next)

    return

dfs(1)
print("yes" if ans!=0 else "Yes")