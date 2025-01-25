import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
graph = [ list(map(int,input().split())) for _ in range(N) ]
dp = [ [0] * N for _ in range(N) ]
dy = [0,0,-1,1]
dx = [-1,1,0,0]

def dfs(y,x):
    if dp[y][x]: return dp[y][x]
    dp[y][x] = 1

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<N and 0<=nx<N and graph[y][x]<graph[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(ny,nx)+1)
    
    return dp[y][x]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i,j))

print(ans)