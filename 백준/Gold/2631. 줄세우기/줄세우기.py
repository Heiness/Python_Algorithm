import sys; input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
nums = [ int(input()) for _ in range(N) ]
ans = [nums[0]]

for v in nums[1:]:
    if ans[-1]<v:ans.append(v)
    else: ans[bisect_left(ans,v)]=v

print(N-len(ans))