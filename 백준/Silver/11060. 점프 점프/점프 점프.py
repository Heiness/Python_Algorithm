import sys;input = sys.stdin.readline
from collections import deque

n = int(input())
nums = list(map(int,input().split()))
dist = [0] * n

q = deque()
q.append(0)


while q:
    now = q.popleft()
    if now == n-1:
        print(dist[now])
        exit()
    for i in range(1,nums[now]+1):
        next = now + i
        if 0<=next<n and not dist[next]:
            dist[next] = dist[now] + 1
            q.append(next)
print(-1)