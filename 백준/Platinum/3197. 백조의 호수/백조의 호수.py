import sys
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Y, X = 0, 1

R, C = map(int, sys.stdin.readline().rstrip().split())
swan = []
water = []
lake = []
for y in range(R):
    lake.append(list(sys.stdin.readline().rstrip()))
    for x in range(C):
        if lake[y][x] == 'L':
            swan.append((y, x))
            lake[y][x] = '.'
        if lake[y][x] == '.':
            water.append((y, x))

visited = [[False]*C for _ in range(R)]
swan_q = [swan[0]] # (y, x)
visited[swan[0][Y]][swan[0][X]] = True

def can_meet():
    global visited
    global swan_q
    
    q = swan_q[:]
    swan_q = []
    while q:
        y, x = q.pop()
        if (y, x) == swan[1]:
            return True
        for dy, dx in DIRS:
            if not (0 <= y+dy < R and 0 <= x+dx < C):
                continue
            if visited[y+dy][x+dx]:
                continue
            if lake[y+dy][x+dx] == 'X':
                visited[y+dy][x+dx] = True # 미리 없애야 swan_q 중복 없어짐. 그리고 (y, x) == swan[1]은 visited된 것에 대해서도 선행 검사하는거라 ㄱㅊ
                swan_q.append((y+dy, x+dx)) # 다음 번엔 백조가 반드시 여길 갈 수 있으니까!
                continue
            visited[y+dy][x+dx] = True
            q.append((y+dy, x+dx))
    return False

def melt_ice():
    global water
    
    q = water[:]
    water = []
    while q:
        y, x = q.pop()
        for dy, dx in DIRS:
            if not (0 <= y+dy < R and 0 <= x+dx < C):
                continue
            if lake[y+dy][x+dx] == 'X':
                water.append((y+dy, x+dx)) # 이번에 처음 녹는 빙하에 의해서만 다음번에 녹는 빙하가 생긴다. 
                lake[y+dy][x+dx] = '.'            

day = 0
while True:
    if can_meet():
        break
    melt_ice()
    day += 1
print(day)