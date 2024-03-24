import sys; input = sys.stdin.readline
from collections import deque

N,M = map(int, input().split())
nums = deque(range(1,N+1))
coms = list(map(int, input().split()))
ans = 0
for c in coms:
    t = nums.index(c)
    if t < (len(nums)+1)/2: 
        nums.rotate(-t)
        ans+=t
        nums.popleft()
    else:
        ans += len(nums)-t
        nums.rotate(len(nums)-t)
        nums.popleft()

print(ans)