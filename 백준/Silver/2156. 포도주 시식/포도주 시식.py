import sys; input = sys.stdin.readline

N = int(input())
nums = [0] * 10001
d = [0] * 10001
for i in range(1,N+1): nums[i] = int(input())
d[1], d[2] = nums[1], nums[1]+nums[2]

for i in range(3,N+1):
    d[i] = max(d[i-2]+nums[i], d[i-1], d[i-3]+nums[i-1]+nums[i])

print(d[N])