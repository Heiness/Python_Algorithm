from itertools import product
from collections import deque
from copy import deepcopy
from pprint import pprint
# 터질 위치 지정 -> 터지는 리스트
# 체크리스트(visited), 폭파리스트
# 터지기

dy = [-1,1,0,0]; dx = [0,0,-1,1]

def find(N, g):
    # global W;
    for i in range(H):
        if g[i][N]!=0: break
    return i
        
def flow(y,x, g):
    p = g[y][x]
    boomList.append((y,x))
    for i in range(4):
        ny = y; nx = x
        for j in range(p-1):
            ny += dy[i]; nx += dx[i]
            if 0<=ny<H and 0<=nx<W and not visited[ny][nx]:
                visited[ny][nx] = True
                searchList.append((ny,nx))

def boom(g):
    while boomList:
        y,x = boomList.pop()
        g[y][x] = 0
        

def down(g):
    for j in range(W):
        for i in range(H-1,-1,-1):
            if g[i][j]==0:
                for k in range(i-1,-1,-1):
                    if g[k][j] !=0: g[i][j], g[k][j] = g[k][j], 0; break
                

def cnt(g):
    c = 0
    for i in range(H):
        for j in range(W):
            if g[i][j]!=0: c+=1
    return c

# 남은 최소 벽돌
T = int(input())

for tc in range(1,T+1):
    N, W, H = map(int,input().split())
    ans = 200 * 200
    graph = [ list(map(int,input().split())) for _ in range(H) ]
    for bl in product(range(W),repeat=N): # 폭탄 순열
        # bl = (2,2,6)
        # print(bl)
        copyGraph = deepcopy(graph)
        for n in bl: # 터질 폭탄 n
            # pprint(copyGraph)
            visited = [[False] * W for _ in range(H)]
            searchList = deque()
            boomList = []
            
            idx = find(n, copyGraph) # 최상단 벽돌 find
            # print("idx ",idx)
            if idx!=-1: searchList.append((idx,n))
            while searchList:
                flow(*searchList.popleft(), copyGraph)
            # print(boomList)
            boom(copyGraph)
            # pprint(copyGraph)
            down(copyGraph)
            # 폭파리스트에 더 넣을 경우가 없으면
            # boom
            # down
        # pprint(copyGraph)
        ans = min(ans,cnt(copyGraph))
        # exit()
    print(f"#{tc} {ans}")
            
    