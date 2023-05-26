import sys; input = sys.stdin.readline

N = int(input())
pair_num = { 0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0 }
ans = 0
dice = [ list(map(int,input().split())) for _ in range(N) ]

for i in range(6): #
    s = 0
    tmp = [ 1,2,3,4,5,6 ]
    tmp.remove(dice[0][i])
    next = dice[0][pair_num[i]]
    tmp.remove(next)
    s+=max(tmp)

    for j in range(1,N):
        tmp = [ 1,2,3,4,5,6 ]
        tmp.remove(next)
        next = dice[j][pair_num[dice[j].index(next)]]
        tmp.remove(next)
        s+=max(tmp)
    
    ans = max(ans,s)

print(ans)