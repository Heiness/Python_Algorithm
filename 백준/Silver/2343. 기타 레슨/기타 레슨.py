import sys; input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
start = max(nums)
end = sum(nums)
ans = sys.maxsize

while start<=end:
    mid = (start+end)//2
    total = 0
    cnt = 1
    for num in nums:
        if total + num > mid:
            # print(f"{num}, {total+num}, {mid}") # 1 2 3 4 5 / 6 7 / 
            cnt+=1
            total = 0
            # continue
        total += num
    # print(ans, cnt, mid)
    
    if cnt <= M:
        # print(f"갱신 {ans}, {mid}, {M}, {cnt}")
        ans = min(ans, mid)
        end = mid -1
    else:
        start = mid + 1
    
print(ans)