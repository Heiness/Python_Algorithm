import sys; input = sys.stdin.readline

def find(x):
    if parent[x]!=x: parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a, b = find(a), find(b)
    if a!=b:
        parent[b] = a
        num[a] += num[b]


for _ in range(int(input())):
    parent = {}
    num = {}
    first = ''
    for __ in range(int(input())): 
        a, b = input().strip().split()
        if not a in parent: 
            parent[a] = a
            num[a] = 1
        if not b in parent: 
            parent[b] = b
            num[b] = 1
        union(a,b)
        print(num[parent[a]])