from collections import deque
def bfs(v):
    Q = deque()
    Q.append([v,0])
    visited[v] = 1

    while Q:
        v,t= Q.popleft()

        if v == G:
            return t

        for w in (v+U, v-D):
            if 1<=w<=F and visited[w] ==0:
                visited[w] = 1
                Q.append([w,t+1])
    return 'use the stairs'


F,S,G,U,D = map(int, input().split())
visited = [0]*(F+1)

if S==G:
    print(0)
elif S==0 and G==0:
    print('use the stairs')
else:
    result = bfs(S)
    print(result)