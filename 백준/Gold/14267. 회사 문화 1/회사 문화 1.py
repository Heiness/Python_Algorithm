import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
score = [0] * (n+1)
graph = [0] + list(map(int,input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    score[a] += b

print("0", end=' ')
for i in range(2,n+1):
    score[i] += score[graph[i]]
    print(f"{score[i]}",end=" ")