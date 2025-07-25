import sys; input = sys.stdin.readline
from collections import deque

MAX_VALUE = 2*100_000+1
N, K = map(int, input().split())
dist = [-1] * MAX_VALUE

q = deque()
q.append(N)
dist[N] = 0

while q:
    now = q.popleft()


    if now == K:
        print(dist[K])
        break

    for nx in [now-1,now+1,now*2]:
        if 0<=nx<MAX_VALUE and dist[nx]==-1:
            dist[nx] = dist[now] + 1
            q.append(nx)
    
