import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M = map(int,input().split())
graph = [ list(input().strip()) for _ in range(N) ]
dp = [ [0] * M for _ in range(N) ]
visited = [ [False] * M for _ in range(N) ]
dy = [0,0,-1,1]
dx = [-1,1,0,0]
dir = ['L','R','U','D']

def dfs(y,x):
    if dp[y][x]==1: return dp[y][x]
    if visited[y][x]: return dp[y][x]
    visited[y][x] = True

    ny = y+dy[dir.index(graph[y][x])]
    nx = x+dx[dir.index(graph[y][x])]

    if 0<=ny<N and 0<=nx<M:
        dp[y][x] = dfs(ny,nx)
    else:
        dp[y][x]=1


    return dp[y][x]

ans = 0 
for i in range(N):
    for j in range(M):
        if dfs(i,j): ans+=1

print(ans)