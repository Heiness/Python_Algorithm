import sys; input = sys.stdin.readline

K, N = map(int, input().split())
nums = []
for i in range(K): nums.append(int(input()))
start, end = 1, max(nums)

while start <= end:
    mid = (start + end) // 2
    res = 0

    for num in nums:
        res += num//mid
    
    if res >= N: start = mid + 1
    else: end = mid - 1

print(end)