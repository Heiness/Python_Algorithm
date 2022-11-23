from collections import deque
n, m = map(int,input().split())

a = list(range(1,n+1))
p = 0
ans = []

while a:
    p+=(m-1)
    if p >= len(a): p = p%len(a)
    ans.append(str(a.pop(p)))

print("<",", ".join(ans),">",sep='')
