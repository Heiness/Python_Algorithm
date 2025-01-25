import sys; input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
nums = [ list(map(int,input().split())) for _ in range(N) ]
nums.sort()
ans = [nums[0][1]]

for v in nums[1:]:
    if v[1]>ans[-1]: ans.append(v[1])
    else: ans[bisect_left(ans,v[1])]=v[1]

print(N-len(ans))