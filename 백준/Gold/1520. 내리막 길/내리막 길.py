import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N) ]
dp = [ [-1] * M for _ in range(N) ]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def dfs(y, x):
    if y==N-1 and x==M-1:
        return 1
    
    if dp[y][x]!=-1:
        return dp[y][x]
    
    tmp = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<N and 0<=nx<M and graph[ny][nx] < graph[y][x]:
            tmp += dfs(ny,nx)
    dp[y][x] = tmp
    return dp[y][x]

print(dfs(0,0))