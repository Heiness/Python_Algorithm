import sys; input = sys.stdin.readline

R, C = map(int,input().split())
graph = [ list(map(lambda x: ord(x)-65, input())) for _ in range(R) ]
visited = [False] * 26
dy = [0,0,-1,1]
dx = [-1,1,0,0]
ans = 1

def dfs(y, x, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<R and 0<=nx<C and not visited[graph[ny][nx]]:
            visited[graph[ny][nx]] = True
            dfs(ny, nx, cnt+1)
            visited[graph[ny][nx]] = False


visited[graph[0][0]] = True
dfs(0,0,ans)
print(ans)