import sys; input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
arr = [ list(map(int,input().strip())) for _ in range(N) ]
visited = [[ [0] * (K+1) for _ in range(M)] for __ in range(N) ]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

q = deque()
q.append((0,0,0))
visited[0][0][0] = 1
res = 1
flag = 0

while q:
    for _ in range(len(q)):
        y, x, c = q.popleft()

        if y==N-1 and x==M-1:
            print(res)
            flag = 1
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<N and 0<=nx<M:
                # 낮이고 벽이 있지만 개수를 다 안부셨을때
                if res%2==1 and arr[ny][nx] == 1 and c<K and not visited[ny][nx][c+1]:
                    visited[ny][nx][c+1] = 1
                    q.append((ny,nx,c+1))

                # 벽이 없을 때
                elif arr[ny][nx] == 0 and not visited[ny][nx][c]:
                    visited[ny][nx][c] = 1
                    q.append((ny,nx,c))

        else: 
            # 밤이고 머무를 때
            if res%2==0: q.append((y,x,c))

    else: res+=1

    if flag: break

else: print(-1)