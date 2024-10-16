import sys; input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
nums.sort() # NlogN
ans = sys.maxsize
ans_nums = [ nums[0], nums[1], nums[2] ]

for i in range(N-2):
    left, right = i+1, N-1
    flag = 1
    while left < right:
        tmp = nums[i] + nums[left] + nums[right]
        if ans > abs(tmp):
            ans = abs(tmp)
            ans_nums = [ nums[i], nums[left], nums[right] ]
            if ans == 0:
                flag = 0
                break
        if tmp > 0 : right-=1
        else: left+=1
    if not flag: break

print(*ans_nums)