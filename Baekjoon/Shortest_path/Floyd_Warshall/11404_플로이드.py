import sys; input = sys.stdin.readline

INF = sys.maxsize
n = int(input())
m = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    dist[i][i] = 0
    
for _ in range(m):
    a,b,c = map(int,input().split())
    dist[a][b] = min(dist[a][b],c)
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j], dist[k][j]+dist[i][k])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j]>=INF: dist[i][j]=0
            
for i in range(1,n+1):
    print(*dist[i][1:])
