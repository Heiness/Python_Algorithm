import sys; input = sys.stdin.readline

N = int(input())
dp = [0] * 31
dp[2] = 3

for i in range(3,N+1):
    if i%2==0: dp[i] = dp[i-2]*3 + sum(dp[:i-2]) * 2 + 2
    else: dp[i] = 0

print(dp[N])