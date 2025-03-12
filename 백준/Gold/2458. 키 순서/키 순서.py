import sys; input = sys.stdin.readline

N, M = map(int,input().split())
visited = [[0]*(N+1) for _ in range(N+1)]
arr = [[] for _ in range(N+1)]
ans = 0

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

def dfs(x, y):
    for i in arr[y]:
        if not visited[x][i]:
            visited[x][i]=1
            visited[i][x]=1
            dfs(x, i)

for i in range(1,N+1): 
    visited[i][i]=1
    dfs(i, i)

for i in range(1,N+1):
    if sum(visited[i])==N: ans+=1

print(ans)