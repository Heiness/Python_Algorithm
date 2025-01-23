import sys; input = sys.stdin.readline
N = int(input())
nums = []

for i in range(N): nums.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(i+1):
        if j==0:
            nums[i][j] = nums[i-1][0]+nums[i][0]
        elif j==i:
            nums[i][j] = nums[i-1][j-1]+nums[i][j]
        else:
            nums[i][j] = max(nums[i-1][j-1],nums[i-1][j])+nums[i][j]

print(max(nums[-1]))