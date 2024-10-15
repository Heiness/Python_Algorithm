import sys; input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

start, end = 0, N-1
lv, rv = nums[start], nums[end]
now = abs(lv+rv)

while start<end:
    tmp = nums[end] + nums[start]

    if now > abs(tmp):
        now = abs(tmp)
        lv, rv = nums[start], nums[end]
        if now == 0: break

    if tmp > 0: end -= 1
    else: start += 1
    

print(lv, rv)