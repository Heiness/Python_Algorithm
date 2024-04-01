import sys; input = sys.stdin.readline

def find(x):
    if parent[x]!=x: parent[x] = find(parent[x])
    return parent[x]

def union(a,b,idx):
    global ans
    a,b = find(a),find(b)
    if a!=b: parent[max(a,b)] = min(a,b)
    elif ans==0: ans = idx

N, M = map(int ,input().split())
parent = list(range(N))
ans = 0

for i in range(M):
    union(*map(int,input().split()),i+1)

print(ans)