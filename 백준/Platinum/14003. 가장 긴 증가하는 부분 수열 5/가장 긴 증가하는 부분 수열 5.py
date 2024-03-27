import sys; input = sys.stdin.readline
from bisect import bisect_left
N = int(input())
*nums, = map(int,input().split())
result = [nums[0]]
cnt = [1]

for v in nums[1:]:
  if result[-1] < v:
    result.append(v)
    cnt.append(len(result))
  else:
    idx = bisect_left(result,v)
    result[idx] = v
    cnt.append(idx+1)

ck = len(result)
ans = []
for i,c in enumerate(cnt[::-1]):
  if ck==0: break
  if c==ck:
    ans.append(nums[N-1-i])
    ck-=1

print(len(result))    
print(*reversed(ans))