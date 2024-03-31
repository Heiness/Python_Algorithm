import sys; input = sys.stdin.readline

N, M = map(int,input().split())
knownList = set(list(map(int,input().split()))[1:])
parties = []
for _ in range(M): parties.append(set(list(map(int,input().split()))[1:]))
for _ in range(M):
    for party in parties: 
        if knownList & party: knownList = knownList.union(party)

ans = 0
for party in parties:
    if knownList & party: continue
    ans+=1
print(ans)