import sys; input = sys.stdin.readline
for tc in range(int(input())):
  left = []
  right = []
  str = input().strip()
  
  for c in str:
    if c=='<':
      if left: right.append(left.pop())
    elif c=='>':
      if right: left.append(right.pop())
    elif c=='-':
      if left: left.pop()
    else: left.append(c)
  
  print("".join(left)+"".join(right[::-1]))