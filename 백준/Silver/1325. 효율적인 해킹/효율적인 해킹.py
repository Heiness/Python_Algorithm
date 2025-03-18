import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    count = 1
    visited = [False] * (N+1)
    visited[start] = True
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for nxt in graph[current]:
            if not visited[nxt]:
                visited[nxt] = True
                count += 1
                queue.append(nxt)
    return count

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 신뢰관계: A B -> B가 해킹당하면 A도 해킹
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

max_hack = 0
result = [0] * (N+1)

for i in range(1, N+1):
    result[i] = bfs(i)
    if result[i] > max_hack:
        max_hack = result[i]

# 최댓값에 해당하는 노드들 출력
for i in range(1, N+1):
    if result[i] == max_hack:
        print(i, end=' ')