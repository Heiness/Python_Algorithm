N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
safe_zone = 0

def dfs(x, y):
    global safe_zone
	
    # 현재 위치 방문처리
    visited[y][x] = True
    # 사이클에 현재 위치 추가
    cycle.append([x, y])
    
    if maps[y][x] == 'U' and y > 0: # 위로
        y -= 1
    elif maps[y][x] == 'D' and y < N-1: # 아래
        y += 1
    elif maps[y][x] == 'L' and x > 0: # 왼쪽
        x -= 1
    elif maps[y][x] == 'R' and x < M-1: # 오른쪽
        x += 1

    if visited[y][x]: # 이동한 위치를 이미 방문한 경우
        if [x, y] in cycle: # 사이클에 이 위치가 포함되어 있다면
            safe_zone += 1 # 사이클이 생겼으므로 세이프 존을 설치해야한다.
    else: # 방문안했으면 다음 위치로
        dfs(x, y)

for x in range(M):
    for y in range(N):
        if not visited[y][x]:
            cycle = []
            dfs(x, y)
            
print(safe_zone)