import sys; input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
ans, ansCnt = 0, 0

def bfs(start):
    global ans, ansCnt
    dist = [0] * 100_001
    tmp = sys.maxsize
    q = deque()
    q.append(start)
    dist[start] = 0

    while q:
        now = q.popleft()

        if now == k:
            ans = dist[now]
            ansCnt+=1
            continue

        for next in [now-1,now+1,now*2]:
            if 0<=next<=100_000 and (dist[next]==0 or dist[next]==dist[now]+1):
                dist[next] = dist[now] + 1
                q.append(next)

bfs(n)
print(ans)
print(ansCnt)