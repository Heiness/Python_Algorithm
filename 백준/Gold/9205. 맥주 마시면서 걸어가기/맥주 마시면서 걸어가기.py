import sys; input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
  N = int(input())
  coord = []
  graph = [[] for _ in range(N+2)]
  coord.append(tuple(map(int,input().split())))
  for i in range(1,N+2):
    coord.append(tuple(map(int,input().split())))
    for idx,(y,x) in enumerate(coord[:-1]):
      t = abs(coord[-1][0] - y) + abs(coord[-1][1] - x)
      if t<=1000:
        graph[i].append(idx)
        graph[idx].append(i)
  q = deque([(0)])
  visited = [False] * (N+2)
  visited[0] = True
  while q:
    now = q.popleft()
    flag = 1
    for n in graph[now]:
      if n==N+1:
        print("happy")
        flag = 0
        break
      if visited[n]: continue
      visited[n] = True
      q.append(n)
    if not flag: break
  if not flag: continue
  print("sad")