import sys; input = sys.stdin.readline

N = int(input())
graph = [ list(map(int,input().split())) for _ in range(N) ]
dp = [ [0] * N for _ in range(N) ]
dp[0][0] = 1

def sol():
    for i in range(N):
        for j in range(N):
            if i==N-1 and j==N-1:
                return
            if i + graph[i][j] < N: dp[i+graph[i][j]][j]+=dp[i][j]
            if j + graph[i][j] < N: dp[i][j+graph[i][j]]+=dp[i][j]

sol()
print(dp[-1][-1])