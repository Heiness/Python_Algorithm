import sys; input = sys.stdin.readline
from collections import Counter

n = int(input())
nums = [ int(input()) for _ in range(n) ]
nums.sort()

print(round(sum(nums)/n))
print(nums[n//2])
c = Counter(nums)
if len(c)==1:
    print(c.most_common(1)[0][0])
else:
    print(c.most_common(2)[1][0]) if (c.most_common(2)[0][1])==(c.most_common(2)[1][1]) else print(c.most_common(1)[0][0])
print(nums[-1]-nums[0])
