import sys

numbers=[]

n = int(input())
for i in range(n):
    k = int(sys.stdin.readline().strip())

    if k == 0: numbers.pop()
    else: numbers.append(k)

print(sum(numbers))
