import sys; input = sys.stdin.readline

N = int(input())
d = [0] * 1001
d[1], d[2] = 1,2

for i in range(3,N+1):
    d[i] = d[i-1]+d[i-2]

print(d[N]%10007)