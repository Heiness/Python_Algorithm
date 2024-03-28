import sys; input = sys.stdin.readline
N = int(input())
ans = 0

for i in range(N):
  s = input().strip()
  if len(s)%2==1: continue
  stack = []
  for c in s:
    if not stack: stack.append(c)
    else:
      if stack[-1] == c: stack.pop()
      else: stack.append(c)
  if not stack: ans+=1
print(ans)