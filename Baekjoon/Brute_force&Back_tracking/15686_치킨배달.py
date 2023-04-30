# 백트래킹 + 브루트포스
import sys; input = sys.stdin.readline
from itertools import combinations

N, M = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N) ]
ch = []
house = []
ans = 1000000

for i in range(N): # 치킨집 좌표 
    for j in range(N):
        if graph[i][j]==2:
            ch.append((i,j))
        elif graph[i][j]==1:
            house.append((i,j))

for c in combinations(ch, M):
    temp = 0

    for h in house:
        ch_len = 10000
        for i in c:
            ch_len = min(ch_len, abs(h[0]-i[0]) + abs(h[1]-i[1]))
        
        temp+=ch_len
    
    ans = min(ans, temp)

print(ans)
