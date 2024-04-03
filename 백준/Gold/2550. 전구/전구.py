import sys; input = sys.stdin.readline
from bisect import bisect_left
N = int(input())
switch = list(map(int,input().split()))
idxSwitch = [0] * (N+1)
for i,v in enumerate(switch): idxSwitch[v] = i
light = list(map(int,input().split()))
nums = [ idxSwitch[v] for v in light ]

res = [nums[0]]; cnt=[1]
l = 1
for v in nums[1:]:
    if res[-1]<v:
        res.append(v)
        l+=1
        cnt.append(l)
    else:
        idx = bisect_left(res,v)
        res[idx] = v
        cnt.append(idx+1)
        
print(l)
ans = []
for i in range(N-1,-1,-1):
    if l==cnt[i]:
        ans.append(light[i])
        l-=1
print(*sorted(ans))