import sys; input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
ans = 0

for i in range(n):
    start, end = 0, n-1
    while start < end:
        tmp = nums[start] + nums[end]
        if tmp==nums[i]:
            if start==i: start+=1
            elif end==i: end-=1
            else:
                ans+=1
                break
        elif tmp < nums[i]: start+=1
        else: end-=1

print(ans)