import sys; input = sys.stdin.readline

def find(x):
    if parent[x]!=x: parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a,b = find(a), find(b)
    if a<b: parent[b]=a
    else: parent[a]=b


N, M = int(input()), int(input())
parent = list(range(N+1))

for i in range(N):
    t = list(map(int,input().split()))
    for idx,v in enumerate(t):
        if i==idx: continue
        if v==1: union(i+1,idx+1)

l = list(map(int,input().split()))
for i in range(len(l)-1):
    if find(l[i])==find(l[i+1]): continue
    print("NO")
    exit()
print("YES")