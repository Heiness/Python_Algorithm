import sys; input = sys.stdin.readline
import copy

dy = [-1,0,1,0]
dx = [0,1,0,-1]
cctv = []
mode = [ [], [[0],[1],[2],[3]], [[0,2],[1,3]], [[0,1],[1,2],[2,3],[3,0]], [[0,1,3],[0,1,2],[1,2,3],[0,2,3]],[[0,1,2,3]]]
graph = []

N, M = map(int,input().split())

for i in range(N):
    data = list(map(int,input().split()))
    graph.append(data)
    for j in range(M):
        if data[j] in [1,2,3,4,5]:
            cctv.append((data[j],i,j))

def fill(arr, d, y, x):
    for i in d:
        ny, nx = y,x
        while True:
            ny+=dy[i]
            nx+=dx[i]
            if ny<0 or ny>=N or nx<0 or nx>=M: break
            elif arr[ny][nx]==6: break
            elif arr[ny][nx]==0: arr[ny][nx]=7


def dfs(depth, arr):
    global min_value

    if depth == len(cctv):
        count = 0
        for i in arr:
            count+=i.count(0)
        min_value = min(min_value, count)
        return

    cctv_num, y, x = cctv[depth]
    temp = copy.deepcopy(arr)
    
    for i in mode[cctv_num]:
        fill(temp, i, y, x)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)

min_value = int(1e9)
dfs(0, graph)
print(min_value)
