import sys; input = sys.stdin.readline
from bisect import bisect_left

def lis(nums):
    res = [nums[0]]
    for v in nums[1:]:
        if res[-1]<v: res.append(v)
        else: res[bisect_left(res,v)]=v
    print(len(res))
    
for t in range(int(input())):
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    lis(nums)