import sys; input = sys.stdin.readline

T = int(input())
z = [0]*41
o = [0]*41
z[0], o[1] = 1, 1

for i in range(2, 41):
    z[i] = z[i-1] + z[i-2]
    o[i] = o[i-1] + o[i-2]

for _ in range(T):
    t = int(input())
    print(z[t], o[t])