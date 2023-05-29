import sys; input = sys.stdin.readline
from copy import deepcopy
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(cnt):
    global min_ans

    if cnt==K:
        q2 = deepcopy(q)
        min_ans = min(min_ans, rotate(q2))
        return
    for i in range(K):
        if visited[i]:
            continue
        visited[i] = 1
        q.append(rotate_center[i])
        dfs(cnt+1)
        visited[i] = 0
        q.pop()

def rotate(q):
    g = deepcopy(graph)
    while q:
        x, y, z = q.popleft()
        lx, ly, rx, ry = x-z, y-z, x+z, y+z
        while True:
            if lx>=rx or ly>=ry:
                break
            dir = 0
            x, y, before = lx, ly, g[lx][ly]
            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]
                if not lx <= nx <= rx or not ly <= ny <= ry:
                    dir += 1
                    continue
                temp = g[nx][ny]
                g[nx][ny] = before
                before = temp
                x, y = nx, ny
                if [x, y] == [lx, ly]:
                    lx += 1; ly += 1; rx -= 1; ry -= 1
                    break
    ans = sys.maxsize
    for row in g:
        ans = min(ans, sum(row))
    return ans

N, M, K = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N) ]

rotate_center = []
for i in range(K):
    r, c, s = map(int, input().split())
    rotate_center.append((r-1,c-1,s))

visited = [0 for _ in range(K)]
q = deque()
min_ans = sys.maxsize
dfs(0)
print(min_ans)