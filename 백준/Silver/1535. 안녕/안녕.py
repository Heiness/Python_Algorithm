import sys; input = sys.stdin.readline
N = int(input())
cache = {0:0}
ans = 0

for w, v in zip(map(int,input().split()), map(int,input().split())):
  tmp = {}
  for i, j in cache.items():
    if w+i < 100 and v+j > cache.get(w+i,0):
      tmp[w+i] = v+j
  cache.update(tmp)
print(max(cache.values()))