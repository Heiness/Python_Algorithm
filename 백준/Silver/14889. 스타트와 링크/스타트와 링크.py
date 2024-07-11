from itertools import combinations
import sys; input = sys.stdin.readline

n = int(input())
t = [ list(map(int,input().split())) for _ in range(n) ]     
p = [ i for i in range(n) ]

team = list(combinations(p,n//2))
# print(team)
result= 1000

for i in range(len(team)//2):
    start = 0
    for x in team[i]:
        for y in team[i]:
            start += t[x][y]
    
    link = 0
    for x in team[-1-i]:
        for y in team[-i-1]:
            link += t[x][y]
    
    result = min(result,abs(start-link))
    
print(result)