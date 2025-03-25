import sys; input = sys.stdin.readline
n = int(input())
graph = [ list(map(int,input().split())) for _ in range(n) ]
ans = sys.maxsize

def dfs(start, now, value, visited):
    global ans
    if len(visited)==n and graph[now][start]:
        ans = min(ans, value+graph[now][start])
        return
    
    for next in range(n):
        if graph[now][next] and not next in visited and value + graph[now][next] < ans:
            dfs(start, next, value + graph[now][next], visited + [next])

for i in range(n):
    dfs(i,i,0,[i])

print(ans)