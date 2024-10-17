import sys; input = sys.stdin.readline

N, M = map(int, input().split())
nums = [ int(input()) for _ in range(N) ]

start, end = max(nums), sum(nums)
ans = sys.maxsize

while start<=end:
    mid = (start+end)//2
    cnt = 1
    total = 0

    for num in nums: # mid로 cnt 세기
        if total + num > mid:
            cnt+=1
            total=0
        total+=num
    
    if M >= cnt:
        ans = mid
        end = mid-1
    else: start = mid + 1

print(ans)