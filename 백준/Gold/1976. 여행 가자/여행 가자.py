import sys; input = sys.stdin.readline

n = int(input())
m = int(input())
parent = list(range(n+1))

def find(x):
    if parent[x]!=x: parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a, b = find(a), find(b)
    if a>b: parent[a] = b
    else: parent[b] = a

for i in range(n):
    tmp = list(map(int, input().split()))
    for idx, j in enumerate(tmp):
        if idx<=i or not j: continue
        union(i+1,idx+1)

plan = list(map(int,input().split()))


def answer():
    t = find(plan[0])
    for p in plan[1:]:
        if t != find(parent[p]):
            print("NO")
            return
    else: print("YES")
    return

answer()