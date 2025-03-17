import sys; input = sys.stdin.readline
from collections import deque

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    nums = list(map(int,input().split()))
    idx = 1
    while nums[idx]!=-1:
        a, b = nums[idx], nums[idx+1]
        graph[nums[0]].append((a,b))
        idx+=2
    
def bfs(start):
    q = deque()
    q.append((0,start))
    visited = [-1] * (V+1)
    visited[start] = 0
    res = [0, 0]

    while q:
        cost, now = q.popleft()
        for v, w in graph[now]:
            if visited[v] == -1:
                nc = cost + w
                q.append((nc, v))
                visited[v] = nc

                if res[1] < nc:
                    res[0], res[1] = v, nc
    
    return res

a, b = bfs(1)
print(bfs(a)[1])