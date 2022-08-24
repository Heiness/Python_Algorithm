from itertools import combinations #조합 함수

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = list(combinations(members, N//2))
m = 100

for i in range(len(possible_team)//2):
    teamA = 0
    for x in possible_team[i]:
        for y in possible_team[i]:
            teamA+=S[x][y]

    teamB = 0
    for x in possible_team[-i-1]:
        for y in possible_team[-i-1]:
            teamB+=S[x][y]

    m = min(m,abs(teamA-teamB))

print(m)

