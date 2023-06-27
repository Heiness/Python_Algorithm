import sys; input = sys.stdin.readline

N, K = map(int,input().split())
items = [(0,0)]
for i in range(N):
    w, v = map(int,input().split())
    items.append((w,v))

graph = [ [0]*(K+1) for _ in range(N+1) ]

for i in range(1,N+1):
    for j in range(1,K+1):
        w = items[i][0]
        v = items[i][1]

        if j < w : graph[i][j] = graph[i-1][j]
        else:
            graph[i][j] = max(graph[i-1][j],v + graph[i-1][j-w])

print(graph[-1][-1])
