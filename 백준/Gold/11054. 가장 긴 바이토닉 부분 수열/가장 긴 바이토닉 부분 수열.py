from bisect import bisect_left
def lis(arr):
    if not arr:return 0
    dp = [arr[0]]
    for i in range(len(arr)):
        if dp[-1]<arr[i]:
            dp.append(arr[i])
        else:
            dp[bisect_left(dp,arr[i])] = arr[i]
    return len(dp)
 
n = int(input())
data = [*map(int,input().split())]
mx = -1
for i in range(n):
    mx = max(mx,lis(data[:i+1])+lis([-i for i in data[i:]])-1)
print(mx)