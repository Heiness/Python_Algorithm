import sys; input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    scores = []
    for _ in range(2):
        scores.append(list(map(int,input().split())))
    for i in range(1,n):
        if i == 1:
            scores[0][i] += scores[1][0]
            scores[1][i] += scores[0][0]
        else:
            scores[0][i] += max(scores[1][i-1],scores[1][i-2])
            scores[1][i] += max(scores[0][i-1],scores[0][i-2])
    print(max(scores[0][-1],scores[1][-1]))
