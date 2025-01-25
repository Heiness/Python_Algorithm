import sys; input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
dp = [0] * 1001
ans = nums[0]
dp[nums[0]] = nums[0]

for i in nums[1:]:
    dp[i] = max(dp[:i])+i
    ans = max(ans,dp[i])

print(ans)