import sys; input = sys.stdin.readline

while 1:
  s = input()[:-1]
  if s=='.': break
  stack = []
  for c in s:
    if c in ['[','(']:
      stack.append(c)
    elif c in [']',')']:
      pair = '[' if c==']' else '('
      if stack and stack[-1]==pair:
        stack.pop()
      else:
        print("no")
        break
  else: print("yes" if not stack else "no")