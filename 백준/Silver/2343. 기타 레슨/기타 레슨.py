import sys; input = sys.stdin.readline

N, M = map(int,input().split())
nums = list(map(int,input().split()))
start = max(nums)
end = sum(nums)


while start<=end:
    mid = (start+end)//2

    count=1
    tmp=0

    for v in nums:
        if tmp + v > mid:
            count += 1
            tmp = 0
        tmp+=v
    if count <= M: end=mid-1
    else: start=mid+1

print(start)