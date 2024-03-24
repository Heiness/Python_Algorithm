import sys; input = sys.stdin.readline
import heapq

def dijk(a, dist):
    pq = []
    heapq.heappush(pq, (0,a))

    while(pq):
        nowW, nowN = heapq.heappop(pq)

        if dist[nowN] < nowW: continue
        dist[nowN] = nowW

        for nextN, nextW in graph[nowN]:
            if H[nowN] < H[nextN]:
                d = nowW+nextW
                if dist[nextN] > d:
                    heapq.heappush(pq,(d,nextN))

N,M,D,E = map(int, input().split()) # 노드, 엣지, 거리비례 체력 소모량, 높이비례 성취감 획득량
H = [-1] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
dist1 = [-1] + [sys.maxsize] * (N)
dist2 = [-1] + [sys.maxsize] * (N)

for i in range(M):
    a, b, c = map(int ,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dijk(1,dist1)
dijk(N,dist2)

ans = -sys.maxsize
for i in range(2,N):
    if(dist1[i] != -sys.maxsize and dist2[i] != -sys.maxsize):
        tmp = dist1[i] + dist2[i]
        ans = max(ans, H[i] * E - tmp * D)

print("Impossible" if ans == -sys.maxsize else ans)