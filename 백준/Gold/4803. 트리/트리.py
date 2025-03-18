import sys
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


T = 0

while True:
    T +=1
    n,m = map(int,input().split())

    if n==0 and m==0:
        break

    parent = [ i for i in range(n+1)]


    cycle = set()

    for i in range(m):
        a,b= map(int,input().split())
        if find(a) == find(b):
            cycle.add(parent[a])
            cycle.add(parent[b])

        if parent[a] in cycle or parent[b] in cycle:
            cycle.add(parent[a])
            cycle.add(parent[b])
        union(a, b)

    for i in range(n+1):
        find(i)

    parent = set(parent)
    ans = sum([1 if i not in cycle else 0 for i in parent])-1

    if ans == 0:
        print('Case %d: No trees.' %T)
    elif ans == 1:
        print('Case %d: There is one tree.' %T)
    else:
        print('Case %d: A forest of %d trees.' %(T,ans))