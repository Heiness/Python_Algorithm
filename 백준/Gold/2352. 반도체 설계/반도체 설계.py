import sys; input = sys.stdin.readline
from bisect import bisect_left
N = int(input())
nums = list(map(int,input().split()))
ans = [nums[0]]

for v in nums:
  if ans[-1] < v: ans.append(v)
  else:
    idx = bisect_left(ans, v)
    ans[idx] = v

print(len(ans))