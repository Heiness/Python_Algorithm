import sys; input = sys.stdin.readline
from itertools import combinations_with_replacement

M, N = map(int,input().split())
for i in combinations_with_replacement(range(1,M+1),N):
    print(*i)