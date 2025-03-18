import sys; input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
dist = [0] * (100_001)
move = [0] * (100_001)

def path(start):
    arr = []
    temp = start
    for _ in range(dist[start]+1):
        arr.append(temp)
        temp = move[temp]
    print(*arr[::-1])

def bfs(start):
    q = deque([start])

    while q:
        now = q.popleft()

        if now == k:
            print(dist[now])
            path(now)
            return 

        for next in [now-1,now+1,now*2]:
            if 0<=next<=100_000 and dist[next]==0:
                dist[next] = dist[now] + 1
                move[next] = now
                q.append(next)

bfs(n)