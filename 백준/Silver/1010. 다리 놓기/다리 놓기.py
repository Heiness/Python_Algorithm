import sys; input = sys.stdin.readline
import math

N = int(input())
for _ in range(N):
    a, b = map(int,input().split())
    print(math.comb(b,a))