import sys; input = sys.stdin.readline
from collections import deque

F, S, G, U, D = map(int,input().split())
dx = [U,-D]
visited = [False] * (F+1)

q = deque()
q.append((S, 0))

while q:
    now, c = q.popleft()
    if now == G:
        print(c)
        break

    for i in range(2):
        next = now + dx[i]

        if 0<next<=F and not visited[next]:
            visited[next] = True
            q.append((next,c+1))
else: print("use the stairs")