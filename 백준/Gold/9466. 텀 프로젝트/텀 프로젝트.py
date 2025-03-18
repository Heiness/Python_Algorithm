import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now):
    global ans
    visited[now] = 1
    cycle.append(now)
    next = connected[now]

    if visited[next]: # 이미 방문된 곳이면 
        if next in cycle: # 사이클 여부 확인
            ans += len(cycle[cycle.index(next):])
        return
    else:
        dfs(next)

T = int(input())
for _ in range(T):
    ans = 0
    N = int(input())
    connected = [0] + list(map(int,input().split()))
    visited = [0] * (N+1)

    for i in range(1,N+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(N - ans)