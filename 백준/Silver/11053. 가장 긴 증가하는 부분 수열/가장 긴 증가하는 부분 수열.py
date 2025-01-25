import sys; input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
nums = list(map(int,input().split()))
tmp = [nums[0]]

for v in nums[1:]:
    if tmp[-1]<v: tmp.append(v)
    else: tmp[bisect_left(tmp,v)] = v

print(len(tmp))