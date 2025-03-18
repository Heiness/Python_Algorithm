import sys; input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
dist = [0] * 100_001

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        
        if now == k:
            return dist[now]


        for next in [now-1,now+1,now*2]:
            if 0<=next<100_001 and (dist[next]==0 or dist[next]>=dist[now]+1):
                dist[next] = dist[now] +1 
                q.append(next)

print(bfs(n))