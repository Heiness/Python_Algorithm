from itertools import combinations

n, m = map(int,input().split())
nums = list(map(int,input().split()))

l = list(combinations(nums,3))
result = 0

for i in l:
    k = sum(i)
    if k<=m and k>result:
        result = k

print(result)

