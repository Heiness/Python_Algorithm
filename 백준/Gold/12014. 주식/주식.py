import sys; input = sys.stdin.readline
from bisect import bisect_left

for t in range(1,int(input())+1):
    print(f"Case #{t}")
    N, K = map(int,input().split())
    nums = list(map(int,input().split()))
    res = [nums[0]]
    for v in nums[1:]:
        if res[-1] < v : res.append(v)
        else: res[bisect_left(res,v)] = v
    print(1 if len(res)>=K else 0)