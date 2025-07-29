import sys; input = sys.stdin.readline

N = int(input())
M = int(input())
edges = [ list(map(int, input().split())) for _ in range(M) ] 
edges.sort(key=lambda x:x[2])
parent = list(range(N+1))

def find(x):
    if parent[x]!=x: parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a, b = find(a),find(b)
    if a>b: parent[b]=a
    else: parent[a]=b

ans=0

for a,b,c in edges:
    if find(a)!=find(b):
        union(a,b)
        ans+=c

print(ans)