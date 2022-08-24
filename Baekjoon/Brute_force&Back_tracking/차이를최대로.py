import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
answer=0

per = list(permutations(nums,n))

for i in per:
    temp=0
    for j in range(0,len(i)-1):
        temp += abs(i[j]-i[j+1])
    answer = max(answer,temp)

print(answer)