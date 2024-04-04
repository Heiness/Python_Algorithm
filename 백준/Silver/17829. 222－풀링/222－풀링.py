n=int(input())
nums=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    nums.append(tmp)
def pooling(size, y, x):
    mid=size//2
    if size==2:
        answer=[nums[y][x], nums[y+1][x], nums[y][x+1], nums[y+1][x+1]]
        answer.sort()
        return answer[-2]
    lt=pooling(mid, y, x)
    rt=pooling(mid, y, x+mid)
    lb=pooling(mid, y+mid, x)
    rb=pooling(mid, y+mid, x+mid)
    answer=[lt, rt, lb, rb]
    answer.sort()
    return answer[-2]
print(pooling(n, 0, 0))