import sys; input = sys.stdin.readline
from bisect import bisect_left

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arrN = list(map(int, input().split()))
    arrM = list(map(int, input().split()))

    arrM.sort()

    ans = 0
    for num in arrN:
        ans += bisect_left(arrM, num)
    
    print(ans)