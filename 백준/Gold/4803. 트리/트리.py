import sys; input = sys.stdin.readline
def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    global cycle
    a, b = find(a), find(b)
    if a==b: cycle.update([a,b])
    elif a in cycle or b in cycle: cycle.update([a,b])
    else: parent[max(a,b)] = min(a,b)
tc = 1

while 1:
    N, M = map(int, input().split())
    if N==0 and M==0: break
    parent = list(range(N+1))
    cycle = set()
    for _ in range(M):
        union(*map(int,input().split()))
    ans = 0
    
    for i in range(1,N+1): find(i)
    trees = set(parent[1:])
    
    for v in trees:
        if v not in cycle: ans+=1
    
    if ans>1: print(f"Case {tc}: A forest of {ans} trees.")
    elif ans==1: print(f"Case {tc}: There is one tree.")
    else: print(f"Case {tc}: No trees.")
    tc += 1