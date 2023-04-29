# deque의 rotate 활용
from collections import deque
import sys; input = sys.stdin.readline

def rotate_right(n: int, d: int):
    if n>4:
        return
    else:
        if wheels[n-1][2] == wheels[n][6]:
            return
        else:
            rotate_right(n+1,-d)
            wheels[n].rotate(-d)

def rotate_left(n: int, d: int):
    if n<1:
        return
    else:
        if wheels[n][2] == wheels[n+1][6]:
            return
        else:
            rotate_left(n-1,-d)
            wheels[n].rotate(-d)

wheels = {}
for i in range(1,5):
    wheels[i] = deque(map(int,input().strip()))

for _ in range(int(input())):
    N, D = map(int,input().split())

    rotate_right(N+1,D)
    rotate_left(N-1,D)

    wheels[N].rotate(D)

ans = 0

for i in range(1,5):
    if wheels[i][0] == 1: ans += 2**(i-1)

print(ans)
