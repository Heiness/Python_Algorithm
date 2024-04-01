import sys; input = sys.stdin.readline
N,M,K = map(int,input().split())
edges = []
for i in range(N):
    edges.append([0])

def find(x):
    if parent[x]!=x: parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a, b = find(a), find(b)
    if a!=b:
        if fc[a]<=fc[b]: parent[b] = a
        else: parent[a] = b

parent = list(range(N+1))
fc = {}
for i, v in enumerate(list(map(int,input().split()))): fc[i+1] = v
for _ in range(M):
    a, b = map(int,input().split())
    union(a,b)

result = 0
friends = set()
for i in parent[1:]:
    if find(i) not in friends:
        friends.add(parent[i])
        result+= fc[parent[i]]
    
print(result if result<=K else "Oh no")