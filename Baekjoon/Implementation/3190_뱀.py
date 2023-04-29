# 경우의 수만 잘 생각하면 되는 간단한 문제
import sys; input = sys.stdin.readline
from collections import deque
from pprint import pprint

dy = [0,1,0,-1]
dx = [1,0,-1,0]

N = int(input())
graph = [ [0] * N for _ in range(N) ] # 0 : 빔 , 1 : 사과 , 2 : 벽 , 3 : 뱀

for _ in range(int(input())): # 사과 설치
    a, b = map(int,input().split())
    graph[a-1][b-1]=1

dc_n = deque() # 방향 전환 저장
dc_d = deque()
for _ in range(int(input())):
    n, d = input().split()
    dc_n.append(int(n))
    dc_d.append(d)

cnt = 0
snake_length = 1
y, x, d = 0, 0, 0
snake = deque([(0,0)])
graph[0][0]=3

def snake_move():
    global N,y,x,d,cnt,snake_length
    ny = y + dy[d]
    nx = x + dx[d]
    if ny<0 or ny>=N or nx<0 or nx>=N :
        print(cnt)
        exit()

    if graph[ny][nx] == 1: # 사과일 경우
        snake.append((ny,nx))
        snake_length+=1
        graph[ny][nx]=3
        y, x = ny, nx

    elif graph[ny][nx] == 0 or (graph[0][0],graph[0][1]) == (ny,nx): # 빈 곳이거나 뱀 마지막
        a, b = snake.popleft()
        snake.append((ny,nx))
        graph[ny][nx]=3
        graph[a][b]=0
        y, x = ny, nx

    elif (ny,nx) in snake: # 벽이거나 뱀 내부일 경우
        print(cnt)
        exit()
        

# for _ in range(4):
while(1):
    # pprint(graph)
    if cnt in dc_n: # 방향 전환 확인
        dc_n.popleft()
        t = dc_d.popleft()

        if t=='D':
            d = (d+1)%4
        elif t=='L':
            d = (d-1)%4

    cnt+=1
    snake_move() # 뱀 이동
