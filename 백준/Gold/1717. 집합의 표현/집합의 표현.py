import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = list(range(n+1))

def find(x):
    if parent[x]!=x: parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a<=b: parent[b] = a
    else: parent[a] = b

for _ in range(m):
    x, y, z = map(int, input().split())
    if x==0: union(y,z)
    else:
        if find(y) == find(z): print("YES")
        else: print("NO")