import sys; input = sys.stdin.readline
from bisect import bisect_right

N, H = map(int,input().split())

arrA = []
arrB = []

for i in range(N):
    if i%2 == 0: arrA.append(-int(input())) 
    else : arrB.append(-int(input()))

arrA.sort()
arrB.sort()

ans = 0
minV = sys.maxsize

for h in range(H):
    tmp = 0
    tmp += bisect_right(arrA, -(h+1))
    tmp += bisect_right(arrB, h-H) 
    if tmp < minV:
        minV = tmp
        ans = 1
    elif tmp == minV:
        ans += 1

print(minV, ans)