import sys; input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
nums = list(map(int,input().split()))
res = [nums[-1]]
for v in nums[-2::-1]:
    if v>res[-1]: res.append(v)
    else:
        idx = bisect_left(res,v)
        res[idx] = v

print(len(res))