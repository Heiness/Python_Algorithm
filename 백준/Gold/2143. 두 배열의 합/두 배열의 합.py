import sys; input = sys.stdin.readline
from bisect import bisect_left, bisect_right

T = int(input())
n = int(input())
arrN = list(map(int, input().split()))
m = int(input())
arrM = list(map(int, input().split()))

sumN, sumM = [], []

# for i in range(n): 
#     for j in range(i+1, n+1): sumN.append(sum(arrN[i:j]))
# for i in range(m):
#     for j in range(i+1, m+1): sumM.append(sum(arrM[i:j]))

for i in range(n):
    temp = arrN[i]
    sumN.append(temp)
    for j in range(i + 1, n):
        temp += arrN[j]
        sumN.append(temp)

for i in range(m):
    temp = arrM[i]
    sumM.append(temp)
    for j in range(i + 1, m):
        temp += arrM[j]
        sumM.append(temp)

sumN.sort()
sumM.sort()

ans = 0

for n in sumN:
    tmp = T - n
    ans += bisect_right(sumM, tmp) - bisect_left(sumM, tmp)

print(ans)