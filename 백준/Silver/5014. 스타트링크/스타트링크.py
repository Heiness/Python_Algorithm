import sys; input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int,input().split())
dist = [0] * (f+1)

def bfs():
    q = deque()
    q.append(s)
    
    while q:
        now = q.popleft()
        if now==g:
            print(dist[now])
            return
    
        for i in (u,-d):
            if not i: continue
            next = now + i
            if next and 0<=next<=f and not dist[next]:
                dist[next] = dist[now] + 1
                q.append(next)
    
    print("use the stairs")

bfs()