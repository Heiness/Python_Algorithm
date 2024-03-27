import sys;input = sys.stdin.readline
N = int(input())
lines = {} # 해쉬가 빠를까, 이차원 배열이 빠를까?
length = [0] * N
for _ in range(N):
  a, b = map(int,input().split())
  lines[a] = b

lines = sorted(lines.items()) # sorted사용시 list로 변환됨.
for i in range(N):
  length[i] = 1
  for j in range(0,i):
    if lines[j][1] < lines[i][1]:
      length[i] = max(length[i], length[j]+1)
      
print(N-max(length))