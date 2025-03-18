import sys;input = sys.stdin.readline
sys.setrecursionlimit(10**8)

r, c, k = map(int, input().split())
graph = [ list(input().strip()) for _ in range(r) ]

dy = [-1,1,0,0]
dx = [0,0,-1,1]
ans = 0

def dfs(y, x, depth):
    global ans
    if depth == k and y == 0 and x == c - 1:
        ans+=1
        return
    
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<r and 0<=nx<c and graph[ny][nx]=='.':
            graph[ny][nx]='T'
            dfs(ny,nx,depth+1)
            graph[ny][nx]='.'

graph[r-1][0] = 'T'
dfs(r-1,0,1)
print(ans)