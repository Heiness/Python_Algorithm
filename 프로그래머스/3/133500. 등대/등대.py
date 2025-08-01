import sys
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):
    from collections import defaultdict

    graph = defaultdict(list)
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        dp[node][0] = 0     # node 꺼짐
        dp[node][1] = 1     # node 켜짐

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                dp[node][0] += dp[neighbor][1]
                dp[node][1] += min(dp[neighbor][0], dp[neighbor][1])

    dfs(1)
    return min(dp[1][0], dp[1][1])
