import sys; input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
graph = [ list(input().strip()) for _ in range(r) ]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def bfs(y, x):
    global a, b
    t1, t2 = 0, 0 # t1은 양, t2는 늑대
    q = deque()
    q.append((y,x))
    if graph[y][x]=='o':
        t1+=1
    elif graph[y][x]=='v':
        t2+=1
    graph[y][x]=0

    while q:
        y,x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0>ny or 0>nx or ny>=r or nx>=c:
                continue
            elif graph[ny][nx]=='.':
                graph[ny][nx]=0
                q.append((ny,nx))
            elif graph[ny][nx]=='o':
                t1+=1
                graph[ny][nx]=0
                q.append((ny,nx))
            elif graph[ny][nx]=='v':
                t2+=1
                graph[ny][nx]=0
                q.append((ny,nx))
    
    if t1>t2:
        a+=t1
    else:
        b+=t2

a, b = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j]!='#':
            bfs(i,j)

print(a,b)
