import sys; input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
dp = [0] * 1001
dp[nums[0]] = nums[0]
ans = nums[0]

for v in nums[1:]:
    dp[v] = max(dp[:v]) + v
    ans = max(ans,dp[v])

print(ans)