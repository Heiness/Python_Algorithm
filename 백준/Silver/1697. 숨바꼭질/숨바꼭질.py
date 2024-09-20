import sys; input = sys.stdin.readline
from collections import deque

N, K = map(int,input().split())

q = deque()
q.append(N)
visited = [-1] * 100001
visited[N] = 0

while q:
    now = q.popleft()

    if now == K:
        print(visited[now])
        break

    if 0<= now*2 <=100000 and visited[now*2] == -1:
        q.append(now*2)
        visited[now*2] = visited[now] + 1
    if 0<= now+1 <=100000 and visited[now+1] == -1:
        q.append(now+1)
        visited[now+1] = visited[now] + 1
    if 0<= now-1 <=100000 and visited[now-1] == -1:
        q.append(now-1)
        visited[now-1] = visited[now] + 1