import sys; input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
# -2 -1 1 4 99

leftV, rightV = nums[0], nums[N-1]
left, right = 0,N-1
ans = abs(nums[left] + nums[right])


while left < right:
    tmp = nums[left] + nums[right]
    if abs(tmp) < ans:
        ans = abs(tmp)
        leftV, rightV = nums[left], nums[right]
        if ans == 0: break
    if tmp < 0: left+=1
    else: right-=1

print(leftV, rightV)